#pragma once

#include <vector>

namespace quantlab {

std::vector<double> cross_sectional_rank(const std::vector<double>& values);
std::vector<double> winsorize(const std::vector<double>& values, double lower_quantile, double upper_quantile);

}  // namespace quantlab
