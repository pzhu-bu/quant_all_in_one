#include "quantlab/factor_engine.hpp"

#include <benchmark/benchmark.h>
#include <vector>

static void BM_CrossSectionalRank(benchmark::State& state) {
  std::vector<double> values(static_cast<std::size_t>(state.range(0)), 0.0);
  for (std::size_t idx = 0; idx < values.size(); ++idx) {
    values[idx] = static_cast<double>((idx * 7919) % 104729);
  }

  for (auto _ : state) {
    benchmark::DoNotOptimize(quantlab::cross_sectional_rank(values));
  }
}

BENCHMARK(BM_CrossSectionalRank)->Arg(1000)->Arg(10000);
