#include "quantlab/optimizer.hpp"

#include <algorithm>
#include <numeric>
#include <vector>

namespace quantlab {

std::vector<double> normalize_long_only_weights(const std::vector<double>& scores) {
  std::vector<double> positive(scores.size());
  std::transform(scores.begin(), scores.end(), positive.begin(), [](double value) {
    return std::max(0.0, value);
  });

  const double total = std::accumulate(positive.begin(), positive.end(), 0.0);
  if (total <= 0.0) {
    return std::vector<double>(scores.size(), 0.0);
  }

  for (double& value : positive) {
    value /= total;
  }
  return positive;
}

}  // namespace quantlab
