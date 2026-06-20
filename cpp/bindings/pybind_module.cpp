#include "quantlab/bsm.hpp"
#include "quantlab/factor_engine.hpp"
#include "quantlab/optimizer.hpp"
#include "quantlab/risk_engine.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(_quantlab_core, module) {
  module.doc() = "C++ acceleration kernels for quantlab";

  module.def("black_scholes_call", &quantlab::black_scholes_call);
  module.def("cross_sectional_rank", &quantlab::cross_sectional_rank);
  module.def("winsorize", &quantlab::winsorize);
  module.def("normalize_long_only_weights", &quantlab::normalize_long_only_weights);
  module.def("historical_var", &quantlab::historical_var);
}
