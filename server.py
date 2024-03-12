from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# Initial data

current_id = 10

car_data = {
    "1": {
        "id": 1,
        "image": "https://vehicle-images.dealerinspire.com/stock-images/chrome/c1b2df90b85a47bbd678f3f50fb77c88.png",
        "make": "Toyota",
        "model": "Prius",
        "year": "2024",
        "fuel_type": "Hybrid",
        "price": "25000",
        "transmission": "Automatic",
        "engine": "2.0L 4-cylinder",
        "mpg_city": "54",
        "mpg_highway": "50",
        "features": ["Backup Camera", "Bluetooth", "Lane Departure Warning"],
        "similar_cars": ["2", "4", "8"],
        "description": "Experience eco-friendly driving with the 2024 Toyota Prius. This Prius boasts a fuel-efficient hybrid engine, achieving an impressive 54 MPG in the city and 50 MPG on the highway. Equipped with modern features like a backup camera, Bluetooth connectivity, and Lane Departure Warning, this Prius ensures a safe enjoyable ride and is a reliable choice for eco-conscious drivers. Be part of the future of driving with the Toyota Prius.",
        "car_type": "Compact"
    },
    "2": {
        "id": 2,
        "image": "https://vehicle-images.dealerinspire.com/stock-images/chrome/76dc251e14b8a7d95e86696996eba04b.png",
        "make": "Toyota",
        "model": "Camry",
        "year": "2024",
        "fuel_type": "Gasoline",
        "price": "28500",
        "transmission": "Automatic",
        "engine": "2.5L 4-cylinder",
        "mpg_city": "29",
        "mpg_highway": "41",
        "features": ["Apple CarPlay", "Android Auto", "Collision Warning"],
        "similar_cars": ["1", "8", "4"],
        "description": "Drive in style and comfort with the 2024 Toyota Camry. This sedan combines a powerful 2.5L 4-cylinder engine with modern features like Apple CarPlay, Android Auto, and Collision Warning. With an impressive 29 MPG in the city and 41 MPG on the highway, the Toyota Camry is a reliable choice for those seeking both performance and efficiency. Be part of the future of driving with the Toyota Camry.",
        "car_type": "Sedan"
    },
    "3": {
        "id": 3,
        "image": "https://vehicle-images.dealerinspire.com/stock-images/chrome/e6255ec87396e9c95542e0c15c7674e4.png",
        "make": "Toyota",
        "model": "Rav4",
        "year": "2024",
        "fuel_type": "Hybrid",
        "price": "32000",
        "transmission": "CVT",
        "engine": "2.5L 4-cylinder",
        "mpg_city": "41",
        "mpg_highway": "38",
        "features": ["Blind Spot Monitor", "Adaptive Cruise Control", "Wireless Charging"],
        "similar_cars": ["5", "7", "6"],
        "description": "Experience the versatility of the 2024 Toyota Rav4 Hybrid. This SUV combines a fuel-efficient hybrid engine with features like Blind Spot Monitor, Adaptive Cruise Control, and Wireless Charging. With a spacious interior and advanced safety features, the Rav4 Hybrid is an ideal choice for those who prioritize both eco-friendliness and functionality.  Be part of the future of driving with the Toyota Rav4.",
        "car_type": "SUV"
    },
    "4": {
        "id": 4,
        "image": "https://www.buyatoyota.com/assets/img/vehicle-info/Corolla/2024/hero-image.png",
        "make": "Toyota",
        "model": "Corolla",
        "year": "2024",
        "fuel_type": "Gasoline",
        "price": "24200",
        "transmission": "Automatic",
        "engine": "1.8L 4-cylinder",
        "mpg_city": "30",
        "mpg_highway": "38",
        "features": ["Lane Keep Assist", "Smart Key System", "Touchscreen Infotainment"],
        "similar_cars": ["1", "2", "8"],
        "description": "Simplify your daily commute with the 2024 Toyota Corolla. This compact car features a fuel-efficient 1.8L 4-cylinder engine and comes equipped with modern conveniences like Lane Keep Assist, Smart Key System, and a Touchscreen Infotainment system. With a sleek design and impressive fuel efficiency, the Corolla is a practical choice for urban driving.  Be part of the future of driving with the Toyota Corolla.",
        "car_type": "Compact"
    },
    "5": {
        "id": 5,
        "image": "https://alcf.s3.us-west-1.amazonaws.com/_custom/2024/toyota/highlander/2024-toyota-grand-highlander%20%287%29.png",
        "make": "Toyota",
        "model": "Highlander",
        "year": "2024",
        "fuel_type": "Hybrid",
        "price": "42500",
        "transmission": "eCVT",
        "engine": "3.5L V6",
        "mpg_city": "36",
        "mpg_highway": "35",
        "features": ["Third-Row Seating", "JBL Premium Audio", "Panoramic Moonroof"],
        "similar_cars": ["5", "3", "6"],
        "description": "Elevate your family adventures with the 2024 Toyota Highlander Hybrid. This SUV combines a powerful 3.5L V6 engine with a hybrid system for enhanced efficiency. With features like Third-Row Seating, JBL Premium Audio, and a Panoramic Moonroof, the Highlander Hybrid ensures a comfortable and enjoyable journey for the whole family. Be part of the future of driving with the Toyota Highlander.",
        "car_type": "SUV"
    },
    "6": {
        "id": 6,
        "image": "https://vehicle-images.dealerinspire.com/stock-images/chrome/e96df23454f979814af5033e5c564f48.png",
        "make": "Toyota",
        "model": "Tacoma",
        "year": "2024",
        "fuel_type": "Gasoline",
        "price": "32900",
        "transmission": "Automatic",
        "engine": "3.5L V6",
        "mpg_city": "19",
        "mpg_highway": "24",
        "features": ["Off-Road Package", "Apple CarPlay", "Toyota Safety Sense"],
        "similar_cars": ["10", "3", "5"],
        "description": "Conquer any terrain with the 2024 Toyota Tacoma. This rugged pickup truck features a powerful 3.5L V6 engine and comes equipped with an Off-Road Package for enhanced capabilities. With modern features like Apple CarPlay and Toyota Safety Sense, the Tacoma is the perfect blend of off-road prowess and advanced technology. Be part of the future of driving with the Toyota Tacoma.",
        "car_type": "Truck"
    },
    "7": {
        "id": 7,
        "image": "https://vehicle-images.dealerinspire.com/stock-images/thumbnails/large/chrome/3afa411bb1d77a2a94967854a4c9f65c.png",
        "make": "Toyota",
        "model": "Sienna",
        "year": "2024",
        "fuel_type": "Hybrid",
        "price": "35500",
        "transmission": "CVT",
        "engine": "2.5L 4-cylinder",
        "mpg_city": "36",
        "mpg_highway": "36",
        "features": ["Dual Power Sliding Doors", "Toyota Entune 3.0", "All-Wheel Drive"],
        "similar_cars": ["3", "5", "6"],
        "description": "Experience family-friendly travel with the 2024 Toyota Sienna Hybrid. This minivan boasts a fuel-efficient hybrid engine, providing both power and efficiency. With features like Dual Power Sliding Doors, Toyota Entune 3.0, and All-Wheel Drive, the Sienna is designed to make family journeys comfortable, convenient, and safe. Be part of the future of driving with the Toyota Sienna.",
        "car_type": "Minivan"
    },
    "8": {
        "id": 8,
        "image": "https://media.chromedata.com/MediaGallery/media/MjkzOTU4Xk1lZGlhIEdhbGxlcnk/mBFi9OSLIrPngN9YruTGgVzM-45Ma_KoApAAexzSP87W6Gmys39x91CUCuaSNqCEqzwCpL8ZYjgQ9vjApPiWDmbA-_k2takwZ-6sci8kzeQBJWZij70GXOqzoX7dgGA4bEoSVfp8DHksGzj_JhTNfoDUmLJqwJoJJ5othtcPPH8vlbHaosUGBg/cc_2024TOC020038_01_640_8Q4.png",
        "make": "Toyota",
        "model": "Avalon",
        "year": "2024",
        "fuel_type": "Gasoline",
        "price": "38900",
        "transmission": "Automatic",
        "engine": "3.5L V6",
        "mpg_city": "22",
        "mpg_highway": "32",
        "features": ["Leather-Trimmed Seats", "Wireless Smartphone Charging", "Blind Spot Monitor"],
        "similar_cars": ["1", "2", "4"],
        "description": "Experience luxury and performance with the 2024 Toyota Avalon. This full-size sedan features a powerful 3.5L V6 engine and offers a range of premium features, including Leather-Trimmed Seats, Wireless Smartphone Charging, and a Blind Spot Monitor. With a stylish exterior and a comfortable interior, the Avalon is a sophisticated choice for discerning drivers. Be part of the future of driving with the Toyota Avalon.",
        "car_type": "Sedan"
    },
    "9": {
        "id": 9,
        "image": "https://www.buyatoyota.com/assets/img/vehicle-info/Supra/2024/hero-image.png",
        "make": "Toyota",
        "model": "Supra",
        "year": "2024",
        "fuel_type": "Gasoline",
        "price": "50000",
        "transmission": "Automatic",
        "engine": "3.0L Inline-6",
        "mpg_city": "22",
        "mpg_highway": "30",
        "features": ["Sport-Tuned Suspension", "Wireless Apple CarPlay", "Brembo Brakes"],
        "similar_cars": ["2", "4", "8"],
        "description": "Unleash the thrill of the track with the 2024 Toyota Supra. This sports car features a powerful 3.0L Inline-6 engine, sport-tuned suspension, and high-performance Brembo brakes. With cutting-edge technology like Wireless Apple CarPlay, the Supra delivers an exhilarating driving experience for enthusiasts. Be part of the future of driving with the Toyota Supra.",
        "car_type": "Sports Car"
    },
    "10": {
        "id": 10,
        "image": "https://dealerimages.dealereprocess.com/image/upload/c_limit,f_auto,fl_lossy,w_500/v1/svp/dep/24toyotatundrahybridlimited/toyota_24tundrahybridlimited_angularfront_magneticgraymetallic",
        "make": "Toyota",
        "model": "Tundra",
        "year": "2024",
        "fuel_type": "Gasoline",
        "price": "45500",
        "transmission": "Automatic",
        "engine": "5.7L V8",
        "mpg_city": "15",
        "mpg_highway": "19",
        "features": ["Towing Package", "Apple CarPlay", "Toyota Safety Sense"],
        "similar_cars": ["6", "5", "3"],
        "description": "Dominate the road with the 2024 Toyota Tundra. This full-size pickup truck is powered by a robust 5.7L V8 engine, making it ideal for towing and hauling. With features like a Towing Package, Apple CarPlay, and Toyota Safety Sense, the Tundra combines power and advanced technology for a reliable and capable driving experience. Be part of the future of driving with the Toyota Tundra.",
        "car_type": "Truck"
    }

}

# Routes

@app.route('/')
def index():
    # List of featured car IDs
    featured_car_ids = ["6", "9", "3"]

    # Get information for featured cars
    featured_cars = {car_id: car_data[car_id] for car_id in featured_car_ids}
    return render_template('index.html', featured_cars=featured_cars)


@app.route('/models')
def models():
    return render_template('models.html', car_data=car_data)


@app.route('/search')
def search():
    query = request.args.get('query', '').lower()

    search_results = [car for car in car_data.values() if query in car['model'].lower()]

    return render_template('search_results.html', query=query, search_results=search_results)


@app.route('/view/<id>')
def view_car(id):
    car = car_data.get(id)
    if car and int(id) <= current_id:
        return render_template('car_details.html', car=car, car_data=car_data)
    else:
        return render_template('car_not_found.html')
    

@app.route('/add', methods=['GET', 'POST'])
def add():
    global current_id
    global car_data

    if request.method == 'POST':
        new_car_data = request.get_json()
        current_id += 1
        new_car_data["id"] = current_id
        new_car_data["make"] = "Toyota"

        car_data[str(current_id)] = new_car_data

        return jsonify(new_car_id=current_id, car_data=car_data)

    return render_template('add.html', current_id=current_id)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_car(id):
    car = car_data.get(id)

    if not car or int(id) > current_id:
        return render_template('car_not_found.html')

    if request.method == 'POST':
        # Check if the form was submitted with the "Discard Changes" button
        if 'discard_changes' in request.form:
            return redirect(url_for('view_car', id=id))

        # Update car data based on the form submission
        car['image'] = request.form['image_url']
        car['model'] = request.form['model']
        car['year'] = int(request.form['year'])
        car['fuel_type'] = request.form['fuel_type']
        car['price'] = request.form['price']
        car['transmission'] = request.form['transmission']
        car['engine'] = request.form['engine']
        car['mpg_city'] = int(request.form['mpg_city'])
        car['mpg_highway'] = int(request.form['mpg_highway'])
        car['features'] = [feature.strip() for feature in request.form['features'].split(',')]
        car['similar_cars'] = [similar_car.strip() for similar_car in request.form['similar_cars'].split(',')]
        car['description'] = request.form['description']
        car['car_type'] = request.form['car_type']

        return redirect(url_for('view_car', id=id))

    return render_template('edit_car.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)