#include "quantlab/factor_engine.hpp"

#include <gtest/gtest.h>
#include <vector>

TEST(FactorEngine, ComputesPercentileRanks) {
  const std::vector<double> values{3.0, 1.0, 2.0};

  const auto ranks = quantlab::cross_sectional_rank(values);

  ASSERT_EQ(ranks.size(), 3);
  EXPECT_DOUBLE_EQ(ranks[0], 1.0);
  EXPECT_DOUBLE_EQ(ranks[1], 1.0 / 3.0);
  EXPECT_DOUBLE_EQ(ranks[2], 2.0 / 3.0);
}
