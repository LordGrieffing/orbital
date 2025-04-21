#include <array>
#include <vector>
#include <cmath>

class massObject{
    public:

        // public attributes
        double mass;
        std::array<double, 3> position;
        std::array<double, 3> velocity;
        double objectRadius;

        // Gravtiational Constant
        double G = 6.674 * pow(10, 11);


        // Constructor
        massObject(double m, const std::array<double, 3>& p, const std::array<double, 3>& v, double r)
            : mass(m), position(p), velocity(p), objectRadius(r){}

        // public function declartion
        std::array<double, 3> accelerate(const std::vector<massObject*> objects, const std::array<double, 3>& offset = {0,0,0}, bool RK = false);
        
};
// Function in charge of calculating acceleration done to an object
std::array<double, 3> massObject::accelerate(const std::vector<massObject*> objects, const std::array<double, 3>& offset = {0,0,0}, bool RK = false){
    
    // Declare temp variables that function uses
    std::array<double, 3> temp_pos = position;
    std::array<double, 3> total_acc = {0, 0, 0};
    std::array<double, 3> r_vec;
    std::array<double, 3> unitV;
    double r_mag;
    double a;


    // Check if offset is zero, if not add the offset to the position of the object 
    if (!isOffsetZero(offset)) {
        for (int i = 0; i < 3; i++){
            position[i] = position[i] + offset[i];
        }
    }

    // Begin looping over all the objects in the system
    for (int i = 0; i < objects.size(); i++){

        // Check to make sure we are not looking at this object
        if(!(objects[i] == this)){
            
            // get the difference vector
            for(int j = 0; j < 3; j++){
                r_vec[j] = position[j] - objects[i]->position[j];
            }

            // get the magnitude of that difference
            r_mag = magnitude(r_vec);

            // construct the unit vector
            for(int j = 0; j < 3; j++){
                unitV[j] = r_vec[j] / r_mag;
            }

            // Calculate acceleration from this current object
            a = -(G * objects[i]->mass) / pow(r_mag, 2);

            // Add this acceleration to the total acceleration on the object
            for(int j = 0; j < 3; j++){
                total_acc[j] = total_acc[j] + (a * unitV[j]);
            }
        }
        // Reset the original position of the object
        for(int j = 0; j < 3; j++){
            position[j] = temp_pos[j];
        }

        // Return the total acceleration happening to the object
        return total_acc;
    }


}

// Checks if offset for acceleration is set to zero
bool isOffsetZero(const std::array<double,3> offset){
    return offset[0] == 0 && offset[1] == 0 && offset[2] == 0;
}

// Finds the magnitude of an array
double magnitude(const std::array<double, 3>& vec){
    return sqrt(pow(vec[0], 2) + pow(vec[1], 2) + pow(vec[2], 2));
}