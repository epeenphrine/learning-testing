package main

import "fmt"

///structs
type car struct {
	gas_pedal      uint16 // uint16: min 0, max 65535
	brake_pedal    uint16
	steering_wheel int16 //int16: min-32768, max 32768
	top_speed_kmh  float64
}

const usixteenbitmax float64 = 65535
const kmh_multiple float64 = 1.60934

func car_struct() {
	
	a_car := car{
		gas_pedal:      16535,
		brake_pedal:    0,
		steering_wheel: 12562,
		top_speed_kmh:  255.0,
	}

	//abbreviation
	// := only for new variables. Use = if using hte variable again
	a_car = car{
		16535,
		0,
		2562,
		255.0,
	}
	fmt.Println("gas pedal:", a_car.gas_pedal, "brake pedal:", a_car.brake_pedal, "steering wheel:", a_car.steering_wheel, "top_speed_kmh:", a_car.top_speed_kmh)

	fmt.Println(a_car.kmh())
	fmt.Println(a_car.mph())

	a_car.new_top_speed(500) //change speed

	fmt.Println(a_car.kmh())
	fmt.Println(a_car.mph())

}

//get a copy of struct, receiever type
func (c car) kmh() float64 {

	return float64(c.gas_pedal) * (c.top_speed_kmh / usixteenbitmax)

}

//get a copy of struct, receiever type
func (c car) mph() float64 {

	return float64(c.gas_pedal) * (c.top_speed_kmh / kmh_multiple / usixteenbitmax)

}

//modify the structed itself via pointer
func (c *car) new_top_speed(newspeed float64) {
	c.top_speed_kmh = newspeed
}

// same thing different way of doing it
func newer_top_speed(c car, speed float64) car {
	c.top_speed_kmh = speed
	return c
}