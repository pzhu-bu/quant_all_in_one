#include "quantlab/optimizer.hpp"

#include <gtest/gtest.h>
#include <numeric>
#include <vector>

TEST(Optimizer, NormalizesPositiveScores) {
  const std::vector<double> scores{-1.0, 2.0, 6.0};

  const auto weights = quantlab::normalize_long_only_weights(scores);
  const double total = std::accumulate(weights.begin(), weights.end(), 0.0);

  EXPECT_DOUBLE_EQ(weights[0], 0.0);
  EXPECT_DOUBLE_EQ(total, 1.0);
}
