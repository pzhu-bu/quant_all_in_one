#pragma once

#include <cstddef>
#include <string>

namespace quantlab {

struct MarketEvent {
  std::string symbol;
  double price = 0.0;
  double volume = 0.0;
};

class EventEngine {
 public:
  void on_market_event(const MarketEvent& event);
  [[nodiscard]] std::size_t event_count() const;
  [[nodiscard]] double traded_notional() const;

 private:
  std::size_t event_count_ = 0;
  double traded_notional_ = 0.0;
};

}  // namespace quantlab
