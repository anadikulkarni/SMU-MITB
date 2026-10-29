"""Generate the Module 5 checkpoint dataset: a deliberately messy sales CSV.

Usage (from the repository root, with your course environment active):

    python checkpoints/module5/make_messy_sales.py

This writes two files next to this script:

    messy_sales.csv            the data you clean (open this one)
    messy_sales_answers.json   the answer key (don't open it until you're done)

The task and the cleaning rules are in COURSE.md, under "Module 5 checkpoint".
Use --seed to generate a different dataset and its matching answer key if you
want a second attempt.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

REGIONS = ["North", "South", "East", "West", "Central"]
CHANNELS = ["Online", "Store"]
PRODUCTS = {  # name: (category, list price, max quantity per order)
    "Laptop": ("Electronics", 1200.00, 2),
    "Monitor": ("Electronics", 250.00, 3),
    "Headphones": ("Electronics", 90.00, 4),
    "Keyboard": ("Accessories", 45.00, 5),
    "Mouse": ("Accessories", 25.00, 6),
    "Webcam": ("Accessories", 60.00, 3),
    "Backpack": ("Accessories", 55.00, 4),
    "Desk": ("Furniture", 300.00, 2),
    "Office Chair": ("Furniture", 180.00, 3),
    "Desk Lamp": ("Furniture", 40.00, 4),
    "Notebook": ("Stationery", 4.50, 20),
    "Pen Set": ("Stationery", 12.00, 10),
}
FIRST = ["Wei", "Priya", "Arjun", "Mei", "Daniel", "Siti", "Rahul", "Hui Min", "James",
         "Aisha", "Kenji", "Nur", "Ethan", "Ananya", "Marcus", "Grace", "Farah", "Ryan"]
LAST = ["Tan", "Lim", "Kumar", "Ng", "Wong", "Rahman", "Lee", "Chen", "Singh", "Ong",
        "Goh", "Iyer", "Koh", "Teo", "Nair", "Chua"]
TEST_NAMES = ["TEST USER", "test account", "Test-Order", "QA testing"]
DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "smu.edu.sg", "example.com.sg"]
DISCOUNTS = [0.0, 0.05, 0.10, 0.15, 0.20]
DISCOUNT_P = [0.55, 0.15, 0.15, 0.10, 0.05]


def make_clean(n, rng):
    """Build the true, clean orders plus flags for the rows the cleaning rules drop."""
    names = list(PRODUCTS)
    product = rng.choice(names, size=n)
    max_qty = np.array([PRODUCTS[p][2] for p in product])
    first = rng.choice(FIRST, size=n)
    last = rng.choice(LAST, size=n)
    df = pd.DataFrame({
        "order_id": [f"ORD-{i:05d}" for i in rng.permutation(np.arange(10000, 10000 + n))],
        "order_date": pd.Timestamp("2025-01-01")
        + pd.to_timedelta(rng.integers(0, 365, size=n), unit="D"),
        "customer_name": [f"{f} {l}" for f, l in zip(first, last)],
        "email": [f"{f.lower().replace(' ', '')}.{l.lower()}{rng.integers(1, 99)}@{rng.choice(DOMAINS)}"
                  for f, l in zip(first, last)],
        "region": rng.choice(REGIONS, size=n, p=[0.25, 0.2, 0.2, 0.2, 0.15]),
        "channel": rng.choice(CHANNELS, size=n, p=[0.6, 0.4]),
        "product": product,
        "category": [PRODUCTS[p][0] for p in product],
        "unit_price": [round(PRODUCTS[p][1] * rng.uniform(0.9, 1.1), 2) for p in product],
        "quantity": rng.integers(1, max_qty + 1).astype(float),
        "discount": rng.choice(DISCOUNTS, size=n, p=DISCOUNT_P),
    })

    is_test = rng.random(n) < 0.015
    df.loc[is_test, "customer_name"] = rng.choice(TEST_NAMES, size=is_test.sum())
    df.loc[is_test, "quantity"] = 99.0

    is_return = (rng.random(n) < 0.03) & ~is_test
    df.loc[is_return, "quantity"] *= -1

    missing_qty = (rng.random(n) < 0.02) & ~is_test & ~is_return
    df.loc[missing_qty, "quantity"] = np.nan

    bad_email = rng.random(n) < 0.04
    breakers = [
        lambda e: e.replace("@", ""),                   # no @
        lambda e: e.replace("@", "@@"),                 # two @
        lambda e: e.replace(".", " ", 1),               # a space inside
        lambda e: e.split("@")[0] + "@" + e.split("@")[1].split(".")[0],  # no dot after @
        lambda e: "@" + e.split("@")[1],                # nothing before @
    ]
    df.loc[bad_email, "email"] = [breakers[rng.integers(len(breakers))](e)
                                  for e in df.loc[bad_email, "email"]]
    return df, bad_email


def answers(clean, bad_email):
    """Apply the cleaning rules to the clean data and compute the answer key."""
    keep = clean.copy()
    keep["bad_email"] = bad_email
    n_test = keep["customer_name"].str.contains("test", case=False).sum()
    keep = keep[~keep["customer_name"].str.contains("test", case=False)]
    n_missing = keep["quantity"].isna().sum()
    keep = keep[keep["quantity"].notna()]
    n_returns = (keep["quantity"] < 0).sum()
    keep = keep[keep["quantity"] > 0]

    keep["net_revenue"] = keep["unit_price"] * keep["quantity"] * (1 - keep["discount"])
    by_month = keep.groupby(keep["order_date"].dt.strftime("%Y-%m"))["net_revenue"].sum()
    by_product = keep.groupby("product")["net_revenue"].sum().sort_values(ascending=False)

    def money(series):
        return {k: round(float(v), 2) for k, v in series.items()}

    return {
        "rows_removed": {
            "test_orders": int(n_test),
            "missing_quantity": int(n_missing),
            "returns": int(n_returns),
        },
        "valid_orders": int(len(keep)),
        "total_net_revenue": round(float(keep["net_revenue"].sum()), 2),
        "net_revenue_by_region": money(keep.groupby("region")["net_revenue"].sum().sort_index()),
        "net_revenue_by_category": money(keep.groupby("category")["net_revenue"].sum().sort_index()),
        "top_3_products": money(by_product.head(3)),
        "best_month": {by_month.idxmax(): round(float(by_month.max()), 2)},
        "mean_order_value_by_channel": money(keep.groupby("channel")["net_revenue"].mean().sort_index()),
        "orders_with_invalid_email": int(keep["bad_email"].sum()),
    }


def messify(clean, rng):
    """Re-write every value in a random messy (but recoverable) format."""
    n = len(clean)
    out = pd.DataFrame({"order_id": clean["order_id"]})

    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%b %d, %Y", "%d-%b-%Y", "%Y%m%d"]
    fmt = rng.choice(date_formats, size=n, p=[0.35, 0.3, 0.15, 0.15, 0.05])
    out["order_date"] = [d.strftime(f) for d, f in zip(clean["order_date"], fmt)]

    def jitter_case(s):
        return [rng.choice([v, v.lower(), v.upper(), f" {v}", f"{v}  "]) for v in s]

    out["customer_name"] = clean["customer_name"].values
    out["email"] = [rng.choice([e, e.upper(), f" {e} "], p=[0.85, 0.1, 0.05])
                    for e in clean["email"]]
    region = jitter_case(clean["region"])
    initials = rng.random(n) < 0.08
    out["region"] = [r.strip()[0].upper() if i else r for r, i in zip(region, initials)]
    out["channel"] = jitter_case(clean["channel"])
    out["product"] = [rng.choice([p, p.lower(), p.upper(), p.replace(" ", "  "), f"{p} "])
                      for p in clean["product"]]
    out["category"] = jitter_case(clean["category"])

    def price(v):
        return rng.choice([f"{v:.2f}", f"${v:,.2f}", f"USD {v:.2f}", f"{v}", f" {v:.2f} "])

    out["unit_price"] = [price(v) for v in clean["unit_price"]]
    out["quantity"] = ["" if np.isnan(q) else f"{int(q)}" for q in clean["quantity"]]

    def discount(d):
        if d == 0:
            return rng.choice(["", "0", "0%"])
        return rng.choice([f"{d:.2f}", f"{d * 100:.0f}%", f"{d:g}"])

    out["discount"] = [discount(d) for d in clean["discount"]]
    return out


def add_duplicates(messy, clean, rng, n_dupes):
    """Append exact copies and re-typed copies (same order, different formatting)."""
    idx = rng.choice(len(messy), size=n_dupes, replace=False)
    exact = messy.iloc[idx[: n_dupes // 2]]
    retyped = messify(clean.iloc[idx[n_dupes // 2:]].reset_index(drop=True), rng)
    both = pd.concat([messy, exact, retyped], ignore_index=True)
    return both.sample(frac=1, random_state=int(rng.integers(1_000_000))).reset_index(drop=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--orders", type=int, default=5000)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    clean, bad_email = make_clean(args.orders, rng)
    key = answers(clean, bad_email)
    messy = messify(clean, rng)
    n_dupes = int(args.orders * 0.03)
    messy = add_duplicates(messy, clean, rng, n_dupes)

    key = {"raw_rows": len(messy), "duplicate_rows_removed": n_dupes, **key}
    args.out.mkdir(parents=True, exist_ok=True)
    messy.to_csv(args.out / "messy_sales.csv", index=False)
    (args.out / "messy_sales_answers.json").write_text(json.dumps(key, indent=2) + "\n")
    print(f"Wrote {len(messy):,} rows to {args.out / 'messy_sales.csv'}")
    print(f"Answer key: {args.out / 'messy_sales_answers.json'} (don't peek!)")


if __name__ == "__main__":
    main()
