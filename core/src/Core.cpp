#include "Core/Core.h"

#include <iostream>

CoreClass::CoreClass(int id) : id_(id) {
}

CoreClass::~CoreClass() = default;

int CoreClass::id() const {
    auto dummy_name = name();
    return id_;
}
