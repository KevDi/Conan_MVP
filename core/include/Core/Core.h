#pragma once

#include <Poco/Notification.h>

#include "export.h"

class DLL_API CoreClass : public Poco::Notification {
   public:
    explicit CoreClass(int id);
    virtual ~CoreClass();
    int id() const;

   private:
    int id_{};
};