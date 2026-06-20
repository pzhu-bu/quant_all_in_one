#include "quantlab/risk_engine.hpp"

#include <algorithm>
#include <cmath>
#include <stdexcept>
#include <vector>

namespace quantlab {

double historical_var(std::vector<double> returns, double confidence) {
  if (!(0.0 < confidence && confidence < 1.0)) {
    throw std::invalid_argument("confidence must be between 0 and 1");
  }
  if (returns.empty()) {
    throw std::invalid_argument("returns must not be empty");
  }

  std::sort(returns.begin(), returns.end());
  const double raw_index = (1.0 - confidence) * static_cast<double>(returns.size() - 1);
  const auto index = static_cast<std::size_t>(std::floor(raw_index));
  return -returns[index];
}

}  // namespace quantlab
