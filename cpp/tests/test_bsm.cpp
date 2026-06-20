#include "quantlab/bsm.hpp"

#include <gtest/gtest.h>

TEST(BlackScholes, MatchesKnownSmokeValue) {
  const double price = quantlab::black_scholes_call(100.0, 100.0, 0.05, 0.2, 1.0);

  EXPECT_NEAR(price, 10.4506, 1e-4);
}
