#include "quantlab/event_engine.hpp"

namespace quantlab {

void EventEngine::on_market_event(const MarketEvent& event) {
  ++event_count_;
  traded_notional_ += event.price * event.volume;
}

std::size_t EventEngine::event_count() const {
  return event_count_;
}

double EventEngine::traded_notional() const {
  return traded_notional_;
}

}  // namespace quantlab
