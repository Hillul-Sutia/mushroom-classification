from flask import Flask, render_template, request
import mushroom_class
import properties as p #contains list of features and their 
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html", cap_shapel=p.cap_shapel,
                           cap_surfacel=p.cap_surfacel, cap_colorl=p.cap_colorl,
                           bruisesl=p.bruisesl, odorl=p.odorl, gill_attachmentl=p.gill_attachmentl,
                           gill_spacingl=p.gill_spacingl, gill_sizel=p.gill_sizel, gill_colorl=p.gill_colorl,
                           stalk_shapel=p.stalk_shapel, stalk_rootl=p.stalk_rootl,
                           stalk_surface_above_ringl=p.stalk_surface_above_ringl,
                           stalk_surface_below_ringl=p.stalk_surface_below_ringl,
                           stalk_color_above_ringl=p.stalk_color_above_ringl,
                           stalk_color_below_ringl=p.stalk_color_below_ringl,
                           veil_colorl=p.veil_colorl, ring_numberl=p.ring_numberl,
                           ring_typel=p.ring_typel, spore_print_colorl=p.spore_print_colorl,
                           populationl=p.populationl, habitatl=p.habitatl)


l = []# For inserting the input of user into the list


def str_to_int(s, col):# for converting the categorical input to numerical input for predicting the output
    i = col.index(s)
    l.append(i)


@app.route('/sub', methods=["POST"])
def submit():

    if request.method == "POST":
        cap_shapei = request.form["cap-shape"]
        cap_surfacei = request.form["cap-surface"]
        cap_colori = request.form["cap-color"]
        bruisesi = request.form["bruises"]
        odori = request.form["odor"]
        gill_attachmenti = request.form["gill-attachment"]
        gill_spacingi = request.form["gill-spacing"]
        gill_sizei = request.form["gill-size"]
        gill_colori = request.form["gill-color"]
        stalk_shapei = request.form["stalk-shape"]
        stalk_rooti = request.form["stalk-root"]
        stalk_surface_above_ringi = request.form["stalk-surface-above-ring"]
        stalk_surface_below_ringi = request.form["stalk-surface-below-ring"]
        stalk_color_above_ringi = request.form["stalk-color-above-ring"]
        stalk_color_below_ringi = request.form["stalk-color-below-ring"]
        veil_colori = request.form["veil-color"]
        ring_numberi = request.form["ring-number"]
        ring_typei = request.form["ring-type"]
        spore_print_colori = request.form["spore-print-color"]
        populationi = request.form["population"]
        habitati = request.form["habitat"]
        l.clear()
        str_to_int(s=cap_shapei, col=p.cap_shape)
        str_to_int(s=cap_surfacei, col=p.cap_surface)
        str_to_int(s=cap_colori, col=p.cap_color)
        str_to_int(s=bruisesi, col=p.bruises)
        str_to_int(s=odori, col=p.odor)
        str_to_int(s=gill_attachmenti, col=p.gill_attachment)
        str_to_int(s=gill_spacingi, col=p.gill_spacing)
        str_to_int(s=gill_sizei, col=p.gill_size)
        str_to_int(s=gill_colori, col=p.gill_color)
        str_to_int(s=stalk_shapei, col=p.stalk_shape)
        str_to_int(s=stalk_rooti, col=p.stalk_root)
        str_to_int(s=stalk_surface_above_ringi, col=p.stalk_surface_above_ring)
        str_to_int(s=stalk_surface_below_ringi, col=p.stalk_surface_below_ring)
        str_to_int(s=stalk_color_above_ringi, col=p.stalk_color_above_ring)
        str_to_int(s=stalk_color_below_ringi, col=p.stalk_color_below_ring)
        str_to_int(s=veil_colori, col=p.veil_color)
        str_to_int(s=ring_numberi, col=p.ring_number)
        str_to_int(s=ring_typei, col=p.ring_type)
        str_to_int(s=spore_print_colori, col=p.spore_print_color)
        str_to_int(s=populationi, col=p.population)
        str_to_int(s=habitati, col=p.habitat)

        user_input = pd.DataFrame(columns=p.features)
        user_input.loc[0] = l

        result = mushroom_class.predict_mushroom_class(user_input)

    return render_template("sub.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
