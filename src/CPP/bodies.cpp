#include <array>
#include <vector>
#include <cmath>
#include <tuple>

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
        std::tuple<std::array<std::array<double, 3>, 4>, std::array<std::array<double, 3>,4>> kUpdate(const std::vector<massObject*> objects, int dt);
        void posVelUpdate(const std::array<std::array<double, 3>,4>& kVel, const std::array<std::array<double, 3>,4>& kPos, int dt);
        
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
    }
    // Reset the original position of the object
        for(int j = 0; j < 3; j++){
            position[j] = temp_pos[j];
        }

    // Return the total acceleration happening to the object
    return total_acc;


}
// Function incharge of updating the k constants for Runge Kutta aproximation
std::tuple<std::array<std::array<double, 3>, 4>, std::array<std::array<double, 3>,4>> massObject::kUpdate(const std::vector<massObject*> objects, int dt){

    // Intialize the k constant variables
    std::array<std::array<double, 3>,4> kPos;
    std::array<std::array<double, 3>,4> kVel;

    // k1
    kVel[0] = accelerate(objects);
    kPos[0] = velocity;

    // k2
    kVel[1] = accelerate(objects, arrayScale(kPos[0], (0.5 * dt)));
    kPos[1] = addArray(velocity, arrayScale(kVel[0], (0.5*dt)));

    // k3 
    kVel[2] = accelerate(objects, arrayScale(kPos[1], (0.5 * dt)));
    kPos[2] = addArray(velocity, arrayScale(kVel[1], (0.5*dt)));

    // k4
    kVel[3] = accelerate(objects, arrayScale(kPos[2], dt));
    kPos[3] = addArray(velocity, arrayScale(kVel[2], dt));

    // Build the tuple for the kConstants
    std::tuple<std::array<std::array<double, 3>, 4>, std::array<std::array<double, 3>,4>> kConstants(kVel, kPos);

    return kConstants;
}

// Function that updates the velocity and position of an object according the RungeKutta aproximation
void massObject::posVelUpdate(const std::array<std::array<double, 3>,4>& kVel, const std::array<std::array<double, 3>,4>& kPos, int dt){

    // Intialize variables
    std::array<double, 3> dV;
    std::array<double, 3> dP;

    // Calculate change in velocity and position
    dV = arrayScale(addArray(addArray(kVel[0], arrayScale(kVel[1], 2)), addArray(arrayScale(kVel[2], 2), kVel[3])), (dt / 6));
    dP = arrayScale(addArray(addArray(kPos[0], arrayScale(kPos[1], 2)), addArray(arrayScale(kPos[2], 2), kPos[3])), (dt / 6));

    // Update position and velocity
    position = addArray(position, dP);
    velocity = addArray(velocity, dV);
}

// Checks if offset for acceleration is set to zero
bool isOffsetZero(const std::array<double,3> offset){
    return offset[0] == 0 && offset[1] == 0 && offset[2] == 0;
}

// Finds the magnitude of an array
double magnitude(const std::array<double, 3>& vec){
    return sqrt(pow(vec[0], 2) + pow(vec[1], 2) + pow(vec[2], 2));
}

// Function used to add two position arrays or velocity arrays
std::array<double, 3> addArray(const std::array<double, 3>& arr1, const std::array<double, 3>& arr2){
    
    std::array<double, 3> arrTot;

    for (int i = 0; i < 3; i++){    
        arrTot[i] = arr1[i] + arr2[i];
    }

    return arrTot;
}

// multiply an array by a scalar
std::array<double, 3> arrayScale(const std::array<double, 3>& arr1, double scalar){

    std::array<double, 3> arrTot;

    for(int i = 0; i < 3; i++){
        arrTot[i] = arr1[i] * scalar;
    }
    return arrTot;
}

