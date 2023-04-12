#include <Consumer/Consumer.h>

int main() {
    CoreClass coreClass{1};
    Consumer consumer{coreClass};

    std::cout << "ID: " << consumer.id() << '\n';
}
