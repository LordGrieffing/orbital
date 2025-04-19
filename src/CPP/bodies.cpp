#include <array>
#include <vector>

class massObject{
    public:

        // public attributes
        double mass;
        std::array<double, 3> position;
        std::array<double, 3> velocity;
        double objectRadius;


        // Constructor
        massObject(double m, const std::array<double, 3>& p, const std::array<double, 3>& v, double r)
            : mass(m), position(p), velocity(p), objectRadius(r){}

        // public function declartion
        std::array<double, 3> accelerateN(const std::vector<massObject> objects, double offset = 0, bool RK = false);
        
};

std::array<double, 3> massObject::accelerateN(const std::vector<massObject> objects, double offset = 0, bool RK = false){
    
}