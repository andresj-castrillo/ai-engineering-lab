## TODOs / challenges

1. Generate a synthetic log dataset (timestamp, status_code, latency_ms), at least 1M rows.
2. Implement a naive Python-loop rolling error-rate calculation. Keep it — it's your correctness baseline, not throwaway code.
3. Implement the same calculation vectorized (cumsum or `sliding_window_view`). Assert the two outputs match.
4. Benchmark both with `time.perf_counter()`, at a few different row counts, and actually look at how the gap changes as n grows.
5. Write the result to Parquet.
6. Challenge: redo the whole pipeline in Polars' lazy API (`pl.scan_csv` → `.collect()`) and compare code and speed to your NumPy version.