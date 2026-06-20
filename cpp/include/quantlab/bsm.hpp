#pragma once

namespace quantlab {

double black_scholes_call(double spot, double strike, double rate, double vol, double time_to_expiry);

}  // namespace quantlab
