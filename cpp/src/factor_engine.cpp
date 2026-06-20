#include "quantlab/factor_engine.hpp"

#include <algorithm>
#include <cstddef>
#include <stdexcept>
#include <utility>
#include <vector>

namespace quantlab {

std::vector<double> cross_sectional_rank(const std::vector<double>& values) {
  if (values.empty()) {
    return {};
  }

  std::vector<std::pair<double, std::size_t>> sorted;
  sorted.reserve(values.size());
  for (std::size_t idx = 0; idx < values.size(); ++idx) {
    sorted.emplace_back(values[idx], idx);
  }
  std::sort(sorted.begin(), sorted.end());

  std::vector<double> ranks(values.size());
  std::size_t start = 0;
  while (start < sorted.size()) {
    std::size_t end = start + 1;
    while (end < sorted.size() && sorted[end].first == sorted[start].first) {
      ++end;
    }

    const double average_rank = (static_cast<double>(start + 1) + static_cast<double>(end)) / 2.0;
    for (std::size_t idx = start; idx < end; ++idx) {
      ranks[sorted[idx].second] = average_rank / static_cast<double>(values.size());
    }
    start = end;
  }

  return ranks;
}

std::vector<double> winsorize(
    const std::vector<double>& values, double lower_quantile, double upper_quantile) {
  if (!(0.0 <= lower_quantile && lower_quantile < upper_quantile && upper_quantile <= 1.0)) {
    throw std::invalid_argument("expected 0 <= lower_quantile < upper_quantile <= 1");
  }
  if (values.empty()) {
    return {};
  }

  std::vector<double> sorted = values;
  std::sort(sorted.begin(), sorted.end());
  const auto lower_idx =
      static_cast<std::size_t>(lower_quantile * static_cast<double>(values.size() - 1));
  const auto upper_idx =
      static_cast<std::size_t>(upper_quantile * static_cast<double>(values.size() - 1));
  const double lower = sorted[lower_idx];
  const double upper = sorted[upper_idx];

  std::vector<double> clipped = values;
  for (double& value : clipped) {
    value = std::clamp(value, lower, upper);
  }
  return clipped;
}

}  // namespace quantlab
