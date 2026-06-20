#include "quantlab/event_engine.hpp"

#include <benchmark/benchmark.h>

static void BM_EventEngineMarketEvent(benchmark::State& state) {
  for (auto _ : state) {
    quantlab::EventEngine engine;
    for (int idx = 0; idx < state.range(0); ++idx) {
      engine.on_market_event({"AAPL", 100.0, 10.0});
    }
    benchmark::DoNotOptimize(engine.traded_notional());
  }
}

BENCHMARK(BM_EventEngineMarketEvent)->Arg(1000)->Arg(10000);
