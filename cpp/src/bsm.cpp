#include "quantlab/bsm.hpp"

#include <cmath>
#include <stdexcept>

namespace quantlab {
namespace {

double norm_cdf(double value) {
  return 0.5 * (1.0 + std::erf(value / std::sqrt(2.0)));
}

}  // namespace

double black_scholes_call(double spot, double strike, double rate, double vol, double time_to_expiry) {
  if (spot <= 0.0 || strike <= 0.0 || vol <= 0.0 || time_to_expiry <= 0.0) {
    throw std::invalid_argument("spot, strike, vol, and time_to_expiry must be positive");
  }

  const double sqrt_t = std::sqrt(time_to_expiry);
  const double d1 =
      (std::log(spot / strike) + (rate + 0.5 * vol * vol) * time_to_expiry) / (vol * sqrt_t);
  const double d2 = d1 - vol * sqrt_t;
  return spot * norm_cdf(d1) - strike * std::exp(-rate * time_to_expiry) * norm_cdf(d2);
}

}  // namespace quantlab
