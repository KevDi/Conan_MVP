#include "Consumer/Consumer.h"

#include <iostream>

Consumer::Consumer(const CoreClass& coreClass) : id_(coreClass.id()) {
}

Consumer::~Consumer() = default;

int Consumer::id() const {
    return id_;
}
