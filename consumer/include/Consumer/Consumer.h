#pragma once

#include <Core/Core.h>

#include "export.h"

class DLL_API Consumer {
   public:
    explicit Consumer(const CoreClass& coreClass);
    virtual ~Consumer();
    int id() const;

   private:
    int id_{};
};