#include <iostream>
#include <string>
using namespace std;

// Base class: Vehicle
class Vehicle {
public:
    // Data members of the base class
    string brand;
    int speed;

    // Constructor to initialize the Vehicle data members
    Vehicle(string b, int s) : brand(b), speed(s) {
        cout << "Vehicle Constructor: " << brand << " created." << endl;
    }

    // Virtual method to display details of the vehicle
    virtual void displayDetails() {
        cout << "Vehicle Brand: " << brand << endl;
        cout << "Vehicle Speed: " << speed << " km/h" << endl;
    }

    // Virtual Destructor
    virtual ~Vehicle() {
        cout << "Vehicle Destructor: " << brand << " destroyed." << endl;
    }
};

// Derived class: Car (inherits from Vehicle)
class Car : public Vehicle {
private:
    string model;  // New data member specific to Car

public:
    // Constructor to initialize both base class and derived class members
    Car(string b, int s, string m) : Vehicle(b, s), model(m) {
        cout << "Car Constructor: " << model << " created." << endl;
    }

    // Method to display details of the car (overrides Vehicle method)
    void displayDetails() override {
        // Calling the base class's method to display common vehicle details
        Vehicle::displayDetails();
        cout << "Car Model: " << model << endl;
    }

    // Method to simulate starting the car's engine
    void startEngine() {
        cout << "The " << model << " car engine is now starting..." << endl;
    }

    // Destructor for the derived class
    ~Car() {
        cout << "Car Destructor: " << model << " destroyed." << endl;
    }
};

// Derived class: ElectricCar (inherits from Car)
class ElectricCar : public Car {
private:
    int batteryLife;  // Data member specific to ElectricCar

public:
    // Constructor to initialize base class members and new members for ElectricCar
    ElectricCar(string b, int s, string m, int battery) : Car(b, s, m), batteryLife(battery) {
        cout << "ElectricCar Constructor: " << m << " (Battery life: " << batteryLife << " hours) created." << endl;
    }

    // Overridden displayDetails() to include battery life
    void displayDetails() override {
        // Calling the base class's method to display common details
        Car::displayDetails();
        cout << "Battery Life: " << batteryLife << " hours" << endl;
    }

    // Overriding startEngine to include electric vehicle specifics
    void startEngine() override {
        cout << "The " << model << " electric car is silently starting..." << endl;
    }

    // Destructor for the ElectricCar
    ~ElectricCar() {
        cout << "ElectricCar Destructor: " << model << " destroyed." << endl;
    }
};

// Main function to demonstrate inheritance
int main() {
    // Creating an object of Vehicle class
    cout << "Creating a Vehicle object..." << endl;
    Vehicle vehicle("Toyota", 120);
    vehicle.displayDetails();
    cout << endl;

    // Creating an object of Car class
    cout << "Creating a Car object..." << endl;
    Car car("Honda", 150, "Civic");
    car.displayDetails();
    car.startEngine();
    cout << endl;

    // Creating an object of ElectricCar class
    cout << "Creating an ElectricCar object..." << endl;
    ElectricCar eCar("Tesla", 200, "Model S", 12);
    eCar.displayDetails();
    eCar.startEngine();
    cout << endl;

    // Demonstrating polymorphism (using base class pointer to call derived class methods)
    Vehicle* vehiclePtr = new ElectricCar("Nissan", 180, "Leaf", 15);
    vehiclePtr->displayDetails();  // Calls ElectricCar's overridden method
    vehiclePtr->startEngine();     // Calls ElectricCar's overridden method

    // Clean up
    delete vehiclePtr;

    return 0;
}

