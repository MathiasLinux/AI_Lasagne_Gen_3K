import os
import urllib
from tkinter import *
from tkinter import ttk
import urllib.parse
import requests
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import keyring
import json
from prestashop import Prestashop, Format
import time
import random
import base64
import sys


# Function to display an error message


def error_window(error_message):
    newerrorwindow = Toplevel(root)
    newerrorwindow.title("Erreur")
    newerrorwindow.geometry("600x200")
    error_img = Image.open("imgs/error.png")
    error_img = error_img.resize((32, 32))
    group_error = ttk.Frame(newerrorwindow)
    label_error = ttk.Label(group_error)
    label_error.image = ImageTk.PhotoImage(error_img)
    label_error['image'] = label_error.image
    label_error.grid(column=0, row=0)
    Label(group_error,
          text=error_message, font=('Arial', 16), foreground="red").grid(column=1, row=0)
    ttk.Button(group_error, text="OK", command=newerrorwindow.destroy).grid(column=1, row=1)
    group_error.grid(column=0, row=0)
    group_error.place(relx=0.5, rely=0.5, anchor="center")


# Function to ping serge api


def ping_serge(url_serge, auth):
    response = requests.post(url_serge + "/ping", auth=auth)

    if response.status_code == 200:
        return True
    else:
        return False


# Function to ping stable diffusion api


def ping_stable_diffusion(url_stable_diffusion, auth):
    response = requests.post(url_stable_diffusion + "/internal/ping", auth=auth)

    if response.status_code == 200:
        return True
    else:
        return False


# Function to open a new window


def optionwindow():
    # Toplevel object which will
    # be treated as a new window
    newoptionwindow = Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newoptionwindow.title("Options")

    # sets the geometry of toplevel
    newoptionwindow.geometry("900x400")

    # Create a grid layout
    frmoption = ttk.Frame(newoptionwindow, padding=10)
    frmoption.grid()

    # A Label widget to show in toplevel
    Label(newoptionwindow,
          text="Options", font=('Arial', 16)).grid(column=1, row=0)

    # Prestashop configuration
    Label(newoptionwindow,
          text="Configuration de Prestashop", font=('Arial', 12)).grid(column=1, row=1)
    Label(newoptionwindow,
          text="URL").grid(column=0, row=2)
    urlpresta = Entry(newoptionwindow, width=50)
    urlpresta.grid(column=1, row=2)
    Label(newoptionwindow,
          text="API Key").grid(column=0, row=3)
    apikeypresta = Entry(newoptionwindow, width=50)
    apikeypresta.grid(column=1, row=3)

    # Serge configuration
    Label(newoptionwindow,
          text="Configuration de Serge", font=('Arial', 12)).grid(column=1, row=4)
    Label(newoptionwindow,
          text="URL").grid(column=0, row=5)
    urlserge = Entry(newoptionwindow, width=50)
    urlserge.grid(column=1, row=5)

    # Serge apache authentification
    Label(newoptionwindow,
          text="Authentification Apache de Serge").grid(column=0, row=6)

    # Serge apache authentification username
    Label(newoptionwindow,
          text="Nom d'utilisateur").grid(column=0, row=7)
    usernamesergeapache = Entry(newoptionwindow, width=50)
    usernamesergeapache.grid(column=1, row=7)

    # Show password
    def showpasswordserge():
        if apachesergepassword.cget('show') == '*':
            apachesergepassword.config(show="")
        else:
            apachesergepassword.config(show="*")

    # Serge apache authentification password
    Label(newoptionwindow,
          text="Mot de passe").grid(column=0, row=8)
    apachesergepassword = Entry(newoptionwindow, width=50, show="*")
    apachesergepassword.grid(column=1, row=8)

    showpasswordbutton = Button(newoptionwindow, text="Afficher le mot de passe", command=showpasswordserge)
    showpasswordbutton.grid(column=2, row=8)

    # Stable Diffusion configuration
    Label(newoptionwindow,
          text="Configuration Stable Diffusion", font=('Arial', 12)).grid(column=1, row=9)
    Label(newoptionwindow,
          text="URL").grid(column=0, row=10)
    urlstable = Entry(newoptionwindow, width=50)
    urlstable.grid(column=1, row=10)

    # Stable Diffusion apache authentification
    Label(newoptionwindow,
          text="Authentification Apache de Stable Diffusion").grid(column=0, row=11)

    # Stable Diffusion apache authentification username
    Label(newoptionwindow,
          text="Nom d'utilisateur").grid(column=0, row=12)
    usernamestableapache = Entry(newoptionwindow, width=50)
    usernamestableapache.grid(column=1, row=12)

    # Show password
    def showpasswordstable():
        if apachestablepassword.cget('show') == '*':
            apachestablepassword.config(show="")
        else:
            apachestablepassword.config(show="*")

    # Stable Diffusion apache authentification password
    Label(newoptionwindow,
          text="Mot de passe").grid(column=0, row=13)
    apachestablepassword = Entry(newoptionwindow, width=50, show="*")
    apachestablepassword.grid(column=1, row=13)

    showpasswordbutton = Button(newoptionwindow, text="Afficher le mot de passe", command=showpasswordstable)
    showpasswordbutton.grid(column=2, row=13)

    # On startup, read the infos.json if it exists and fill the fields it contains by decrypting them

    try:
        with open('infos.json') as json_file:
            data = json.load(json_file)
            # Decrypt all the infos
            urlprestaencrypt = data['urlpresta'].encode('utf-8')
            apikeyprestaencrypt = data['apikeypresta'].encode('utf-8')
            urlsergeencrypt = data['urlserge'].encode('utf-8')
            usernamesergeapacheencrypt = data['usernamesergeapache'].encode('utf-8')
            apachesergepasswordencrypt = data['apachesergepassword'].encode('utf-8')
            urlstableencrypt = data['urlstable'].encode('utf-8')
            usernamestableapacheencrypt = data['usernamestableapache'].encode('utf-8')
            apachestablepasswordencrypt = data['apachestablepassword'].encode('utf-8')
            # Decrypt the infos using the key
            # Get the key from the keyring

            key = keyring.get_password("AI Lasagne Generator 3000", "key")
            f = Fernet(key.encode('utf-8'))
            urlprestadecoded = f.decrypt(urlprestaencrypt).decode('utf-8')
            apikeyprestadecoded = f.decrypt(apikeyprestaencrypt).decode('utf-8')
            urlsergedecoded = f.decrypt(urlsergeencrypt).decode('utf-8')
            usernamesergeapachedecoded = f.decrypt(usernamesergeapacheencrypt).decode('utf-8')
            apachesergepassworddecoded = f.decrypt(apachesergepasswordencrypt).decode('utf-8')
            urlstabledecoded = f.decrypt(urlstableencrypt).decode('utf-8')
            usernamestableapachedecoded = f.decrypt(usernamestableapacheencrypt).decode('utf-8')
            apachestablepassworddecoded = f.decrypt(apachestablepasswordencrypt).decode('utf-8')
            # Fill the fields

            urlpresta.insert(0, urlprestadecoded)
            apikeypresta.insert(0, apikeyprestadecoded)
            urlserge.insert(0, urlsergedecoded)
            usernamesergeapache.insert(0, usernamesergeapachedecoded)
            apachesergepassword.insert(0, apachesergepassworddecoded)
            urlstable.insert(0, urlstabledecoded)
            usernamestableapache.insert(0, usernamestableapachedecoded)
            apachestablepassword.insert(0, apachestablepassworddecoded)

    except FileNotFoundError:
        error_window("Fichier infos.json introuvable. \n Veuillez configurer l'application")
    except Exception as e:
        error_window("Erreur lors de la lecture du fichier infos.json. \n Veuillez configurer l'application")

    # Save button
    def save():
        # Save the infos in a encrypted json file
        # Encrypt all the infos
        key = Fernet.generate_key()
        keyring.set_password("AI Lasagne Generator 3000", "key", key.decode('utf-8'))
        f = Fernet(key)
        urlprestaencrypt = f.encrypt(urlpresta.get().encode('utf-8'))
        apikeyprestaencrypt = f.encrypt(apikeypresta.get().encode('utf-8'))
        urlsergeencrypt = f.encrypt(urlserge.get().encode('utf-8'))
        usernamesergeapacheencrypt = f.encrypt(usernamesergeapache.get().encode('utf-8'))
        apachesergepasswordencrypt = f.encrypt(apachesergepassword.get().encode('utf-8'))
        urlstableencrypt = f.encrypt(urlstable.get().encode('utf-8'))
        usernamestableapacheencrypt = f.encrypt(usernamestableapache.get().encode('utf-8'))
        apachestablepasswordencrypt = f.encrypt(apachestablepassword.get().encode('utf-8'))
        # Write the infos in the file
        with open('infos.json', 'w') as outfile:
            json.dump({
                'urlpresta': urlprestaencrypt.decode('utf-8'),
                'apikeypresta': apikeyprestaencrypt.decode('utf-8'),
                'urlserge': urlsergeencrypt.decode('utf-8'),
                'usernamesergeapache': usernamesergeapacheencrypt.decode('utf-8'),
                'apachesergepassword': apachesergepasswordencrypt.decode('utf-8'),
                'urlstable': urlstableencrypt.decode('utf-8'),
                'usernamestableapache': usernamestableapacheencrypt.decode('utf-8'),
                'apachestablepassword': apachestablepasswordencrypt.decode('utf-8')
            }, outfile)
        newoptionwindow.destroy()

    savebutton = Button(newoptionwindow, text="Sauvegarder", command=save, font=('Arial', 12))
    savebutton.grid(column=1, row=14)


# Function to get the last product created

def get_last_product():
    # Get the last product created
    # Get the infos from the file
    try:
        with open('infos.json') as json_file:
            data = json.load(json_file)
            # We verify if the variables exist
            if not data['urlpresta'] or not data['apikeypresta']:
                error_window("Veuillez configurer l'application")
                return

            # Decrypt all the infos
            urlprestaencrypt = data['urlpresta'].encode('utf-8')
            apikeyprestaencrypt = data['apikeypresta'].encode('utf-8')
            # Decrypt the infos using the key
            # Get the key from the keyring

            key = keyring.get_password("AI Lasagne Generator 3000", "key")
            f = Fernet(key.encode('utf-8'))
            try:
                urlprestadecoded = f.decrypt(urlprestaencrypt).decode('utf-8')
                apikeyprestadecoded = f.decrypt(apikeyprestaencrypt).decode('utf-8')
            except Exception as e:
                error_window("Erreur lors de la lecture du fichier infos.json. \n Veuillez configurer l'application")
                return

            # Using the infos, get the last product created from the Prestashop API with the prestashop module

            api = Prestashop(
                url=urlprestadecoded,
                api_key=apikeyprestadecoded,
                default_lang=1,
                debug=True,
                data_format=Format.JSON,
            )

            # Verify that the connection is working with ping
            try:
                api.ping()

            except Exception as e:
                error_window(
                    "Erreur lors de la connexion à l'API de Prestashop. \n Veuillez verifier la configuration de celle-ci.")
                return

            # Get the last product created
            lastproduct = api.search('products', sort='[id_DESC]', limit=1)

            # Get the name of the product
            if lastproduct and lastproduct['products'][0] and lastproduct['products'][0]['name']:
                productName = lastproduct['products'][0]['name']

                # We verify that we get the product
                if productName != "":
                    # Display the name of the product under the bouton
                    ttk.Label(frm, text="Dernier produit crée : ", font=('Arial-bold', 12)).grid(column=0, row=7)
                    ttk.Label(frm, text=productName, font=('Arial', 12)).grid(column=0, row=8)

    except FileNotFoundError:
        error_window("Fichier infos.json introuvable. \n Veuillez configurer l'application")


# Function to create the products


def create_products(newverifywindow=None):
    # Close the window for the verification
    if newverifywindow:
        newverifywindow.destroy()

    # If the window is already open, we destroy it
    try:
        newprogresswindow
    except NameError:
        print("Window not open")
    else:
        newprogresswindow.destroy()

    # Create a window to display the progress of the creation of the products using the tkinter module
    newprogresswindow = Toplevel(root)
    newprogresswindow.title("Création des produits")
    newprogresswindow.geometry("900x600")
    # We create a group to store all the elements
    group_progress = ttk.Frame(newprogresswindow)
    # We create a group for the title
    group_title = ttk.Frame(group_progress)
    # We add the title
    Label(group_title,
          text="Création des produits", font=('Arial', 16)).grid(column=0, row=0)
    group_title.grid(column=0, row=0)
    # We create a group for the progress bar
    group_progressbar = ttk.Frame(group_progress)
    # We add the progress bar
    progressbar = ttk.Progressbar(group_progressbar, orient=HORIZONTAL, length=300, mode='determinate')
    progressbar.grid(column=0, row=0)
    group_progressbar.grid(column=0, row=1)
    # We create a group to store a table which containers all the etapes of the creation of the products with a check or a cross or a loading gif they reset at each product
    group_table = ttk.Frame(group_progress)
    # We add the title
    Label(group_table,
          text="Etapes", font=('Arial-bold', 16)).grid(column=0, row=2)
    Label(group_table,
          text="Statut", font=('Arial-bold', 16)).grid(column=1, row=2)

    # We add the title
    Label(group_table,
          text="Connexion à Prestashop", font=('Arial', 16)).grid(column=0, row=3)
    # We add the image
    img_prestashop = Image.open("imgs/loading.png")
    img_prestashop = img_prestashop.resize((24, 32))
    label_prestashop = ttk.Label(group_table)
    label_prestashop.image = ImageTk.PhotoImage(img_prestashop)
    label_prestashop['image'] = label_prestashop.image
    label_prestashop.grid(column=1, row=3)

    # We add the title
    Label(group_table,
          text="Connexion à Serge", font=('Arial', 16)).grid(column=0, row=4)
    # We add the image
    img_serge = Image.open("imgs/loading.png")
    img_serge = img_serge.resize((24, 32))
    label_serge = ttk.Label(group_table)
    label_serge.image = ImageTk.PhotoImage(img_serge)
    label_serge['image'] = label_serge.image
    label_serge.grid(column=1, row=4)

    # We add the title
    Label(group_table,
          text="Connexion à Stable Diffusion", font=('Arial', 16)).grid(column=0, row=5)
    # We add the image
    img_stable = Image.open("imgs/loading.png")
    img_stable = img_stable.resize((24, 32))
    label_stable = ttk.Label(group_table)
    label_stable.image = ImageTk.PhotoImage(img_stable)
    label_stable['image'] = label_stable.image
    label_stable.grid(column=1, row=5)

    # We add the title
    Label(group_table,
          text="Création du texte du produit dans Serge", font=('Arial', 16)).grid(column=0, row=6)
    # We add the image
    img_serge_creation = Image.open("imgs/loading.png")
    img_serge_creation = img_serge_creation.resize((24, 32))
    label_serge_creation = ttk.Label(group_table)
    label_serge_creation.image = ImageTk.PhotoImage(img_serge_creation)
    label_serge_creation['image'] = label_serge_creation.image
    label_serge_creation.grid(column=1, row=6)

    # We add the title
    Label(group_table,
          text="Création des images dans Stable Diffusion", font=('Arial', 16)).grid(column=0, row=7)
    # We add the image
    img_stable_creation = Image.open("imgs/loading.png")
    img_stable_creation = img_stable_creation.resize((24, 32))
    label_stable_creation = ttk.Label(group_table)
    label_stable_creation.image = ImageTk.PhotoImage(img_stable_creation)
    label_stable_creation['image'] = label_stable_creation.image
    label_stable_creation.grid(column=1, row=7)

    # We add the title
    Label(group_table,
          text="Ajout du produit dans Prestashop", font=('Arial', 16)).grid(column=0, row=8)
    # We add the image
    img_prestashop_creation = Image.open("imgs/loading.png")
    img_prestashop_creation = img_prestashop_creation.resize((24, 32))
    label_prestashop_creation = ttk.Label(group_table)
    label_prestashop_creation.image = ImageTk.PhotoImage(img_prestashop_creation)
    label_prestashop_creation['image'] = label_prestashop_creation.image
    label_prestashop_creation.grid(column=1, row=8)

    # We add the title
    Label(group_table,
          text="Ajout des images dans Prestashop", font=('Arial', 16)).grid(column=0, row=9)
    # We add the image
    img_prestashop_images = Image.open("imgs/loading.png")
    img_prestashop_images = img_prestashop_images.resize((24, 32))
    label_prestashop_images = ttk.Label(group_table)
    label_prestashop_images.image = ImageTk.PhotoImage(img_prestashop_images)
    label_prestashop_images['image'] = label_prestashop_images.image
    label_prestashop_images.grid(column=1, row=9)

    # We add the title
    Label(group_table,
          text="Ajout du stock dans Prestashop", font=('Arial', 16)).grid(column=0, row=10)
    # We add the image
    img_prestashop_stock = Image.open("imgs/loading.png")
    img_prestashop_stock = img_prestashop_stock.resize((24, 32))
    label_prestashop_stock = ttk.Label(group_table)
    label_prestashop_stock.image = ImageTk.PhotoImage(img_prestashop_stock)
    label_prestashop_stock['image'] = label_prestashop_stock.image
    label_prestashop_stock.grid(column=1, row=10)

    # We add the title
    Label(group_table,
          text="Mise à jour de l'attribut du produit dans Prestashop", font=('Arial', 16)).grid(column=0, row=11)
    # We add the image
    img_prestashop_attribute = Image.open("imgs/loading.png")
    img_prestashop_attribute = img_prestashop_attribute.resize((24, 32))
    label_prestashop_attribute = ttk.Label(group_table)
    label_prestashop_attribute.image = ImageTk.PhotoImage(img_prestashop_attribute)
    label_prestashop_attribute['image'] = label_prestashop_attribute.image
    label_prestashop_attribute.grid(column=1, row=11)

    # We add the title
    Label(group_table,
          text="Suppression du chat dans Serge", font=('Arial', 16)).grid(column=0, row=12)
    # We add the image
    img_serge_delete = Image.open("imgs/loading.png")
    img_serge_delete = img_serge_delete.resize((24, 32))
    label_serge_delete = ttk.Label(group_table)
    label_serge_delete.image = ImageTk.PhotoImage(img_serge_delete)
    label_serge_delete['image'] = label_serge_delete.image
    label_serge_delete.grid(column=1, row=12)

    # We add a button to close the window
    ttk.Button(group_table, text="Fermer", command=newprogresswindow.destroy).grid(column=0, row=13)

    group_table.grid(column=0, row=2)
    group_progress.grid(column=0, row=0)
    group_progress.place(relx=0.5, rely=0.5, anchor="center")

    newprogresswindow.update()

    # We get the url and the api key from the file
    try:
        # We verify that the file exists
        os.path.isfile('infos.json')
    except FileNotFoundError:
        error_window("Fichier infos.json introuvable. \n Veuillez configurer l'application")
        return

    with open('infos.json') as json_file:
        data = json.load(json_file)
        # Decrypt all the infos
        urlprestaencrypt = data['urlpresta'].encode('utf-8')
        apikeyprestaencrypt = data['apikeypresta'].encode('utf-8')
        urlsergeencrypt = data['urlserge'].encode('utf-8')
        usernamesergeapacheencrypt = data['usernamesergeapache'].encode('utf-8')
        apachesergepasswordencrypt = data['apachesergepassword'].encode('utf-8')
        urlstableencrypt = data['urlstable'].encode('utf-8')
        usernamestableapacheencrypt = data['usernamestableapache'].encode('utf-8')
        apachestablepasswordencrypt = data['apachestablepassword'].encode('utf-8')
        # Decrypt the infos using the key
        # Get the key from the keyring

        key = keyring.get_password("AI Lasagne Generator 3000", "key")
        f = Fernet(key.encode('utf-8'))
        urlprestadecoded = f.decrypt(urlprestaencrypt).decode('utf-8')
        apikeyprestadecoded = f.decrypt(apikeyprestaencrypt).decode('utf-8')
        urlsergedecoded = f.decrypt(urlsergeencrypt).decode('utf-8')
        usernamesergeapachedecoded = f.decrypt(usernamesergeapacheencrypt).decode('utf-8')
        apachesergepassworddecoded = f.decrypt(apachesergepasswordencrypt).decode('utf-8')
        urlstabledecoded = f.decrypt(urlstableencrypt).decode('utf-8')
        usernamestableapachedecoded = f.decrypt(usernamestableapacheencrypt).decode('utf-8')
        apachestablepassworddecoded = f.decrypt(apachestablepasswordencrypt).decode('utf-8')

        # Using the infos, get the last product created from the Prestashop API with the prestashop module

        api = Prestashop(
            url=urlprestadecoded,
            api_key=apikeyprestadecoded,
            default_lang=1,
            debug=True,
            data_format=Format.JSON,
        )

        serge_params_creation = {
            "model": "Vicuna-13B",
            "temperature": 0.1,
            "top_k": 50,
            "top_p": 0.95,
            "max_length": 2048,
            "context_window": 2048,
            "gpu_layers": 0,
            "repeat_last_n": 64,
            "repeat_penalty": 1.3,
            "init_prompt": "Below is an instruction that describes a task. Write a response that exactly completes the request, with the requested structure.",
            "n_threads": 4,
        }

        # Verify that the connection is working with ping
        try:
            api.ping()

        except Exception as e:
            # Display a window to inform the user that the connection failed using the tkinter module
            # We check the connection to Prestashop and we display a cross
            img_prestashop = Image.open("imgs/error.png")
            img_prestashop = img_prestashop.resize((24, 32))
            label_prestashop.image = ImageTk.PhotoImage(img_prestashop)
            label_prestashop['image'] = label_prestashop.image
            newprogresswindow.update()
            error_window(
                "Erreur lors de la connexion à l'API de Prestashop. \n Veuillez verifier la configuration de celle-ci.")
            return

        try:
            ping_serge(urlsergedecoded, (usernamesergeapachedecoded, apachesergepassworddecoded))
        except Exception as e:
            img_serge = Image.open("imgs/error.png")
            img_serge = img_serge.resize((24, 32))
            label_serge.image = ImageTk.PhotoImage(img_serge)
            label_serge['image'] = label_serge.image
            newprogresswindow.update()
            error_window(
                "Erreur lors de la connexion à l'API de Serge. \n Veuillez verifier la configuration de celle-ci.")
            return

        try:
            ping_stable_diffusion(urlstabledecoded, (usernamestableapachedecoded, apachestablepassworddecoded))
        except Exception as e:
            img_stable = Image.open("imgs/error.png")
            img_stable = img_stable.resize((24, 32))
            label_stable.image = ImageTk.PhotoImage(img_stable)
            label_stable['image'] = label_stable.image
            newprogresswindow.update()
            error_window(
                "Erreur lors de la connexion à l'API de Stable Diffusion. \n Veuillez verifier la configuration de celle-ci.")
            return

        # We check the connection to Prestashop and we display a check
        # We also check the connection to Serge, and we display a check
        # We also check the connection to Stable Diffusion, and we display a check
        img_prestashop = Image.open("imgs/check.png")
        img_prestashop = img_prestashop.resize((24, 32))
        label_prestashop.image = ImageTk.PhotoImage(img_prestashop)
        label_prestashop['image'] = label_prestashop.image
        img_serge = Image.open("imgs/check.png")
        img_serge = img_serge.resize((24, 32))
        label_serge.image = ImageTk.PhotoImage(img_serge)
        label_serge['image'] = label_serge.image
        img_stable = Image.open("imgs/check.png")
        img_stable = img_stable.resize((24, 32))
        label_stable.image = ImageTk.PhotoImage(img_stable)
        label_stable['image'] = label_stable.image
        newprogresswindow.update()

        if (scale_value.get() == ""):
            error_window("Veuillez entrer un nombre de produits à créer")
            return

        for i in range(0, int(scale_value.get())):
            # We create our chat

            response = requests.post(urlsergedecoded + "/chat", params=serge_params_creation,
                                     auth=(usernamesergeapachedecoded, apachesergepassworddecoded))

            # We get the last added product
            lastproduct = api.search('products', sort='[id_DESC]', limit=1)

            lastproduct = lastproduct['products'][0]['name']

            # remove the "
            chat_id = response.text.replace("\"", "")

            # We check if the user has specified a product to create or a category

            if category_value.get() != "" and product_value.get() != "":
                error_window("Veuillez entrer soit une catégorie soit un produit à créer")
                return

            if category_value.get() != "" and product_value.get() == "":
                params_first_request = {
                    "prompt": 'You are an expert in vintage products. Create a new vintage product, in the "' + category_value.get() + '" category, not a "' + lastproduct + '" in French, with an english title, a French title, an english description, a French description. All the infos must be separeted with a pipe |. Respect this exact structure : titleEN|titleFR|descriptionEN|descriptionFR. Only output the values, no other text is authorized. Use the pipe | between all the values and only that. For example : Vintage Bag|Sac vintage|A vintage bag|Un sac vintage'
                }
            elif product_value.get() != "" and category_value.get() == "":
                params_first_request = {
                    "prompt": 'You are an expert in vintage products. Create a "' + product_value.get() + '", with an english title, a French title, an english description, a French description. All the infos must be separeted with a pipe |. Respect this exact structure : titleEN|titleFR|descriptionEN|descriptionFR. Only output the values, no other text is authorized. Use the pipe | between all the values and only that. For example : Vintage Bag|Sac vintage|A vintage bag|Un sac vintage'
                }
            else:
                params_first_request = {
                    "prompt": 'You are an expert in vintage products. Create a new vintage product, not a "' + lastproduct + '" in French, with an english title, a French title, an english description, a French description. All the infos must be separeted with a pipe |. Respect this exact structure : titleEN|titleFR|descriptionEN|descriptionFR. Only output the values, no other text is authorized. Use the pipe | between all the values and only that. For example : Vintage Bag|Sac vintage|A vintage bag|Un sac vintage'
                }

            # We verify that the url does not end with a /, if it does, we remove it

            if urlsergedecoded.endswith("/"):
                real_url = urlsergedecoded + "chat/" + chat_id + "/question"
            else:
                real_url = urlsergedecoded + "/chat/" + chat_id + "/question"

            urllib.parse.quote(real_url)

            time.sleep(2)

            # We make the request to Serge
            response = requests.post(real_url, params=params_first_request,
                                     auth=(usernamesergeapachedecoded, apachesergepassworddecoded))

            if response.status_code != 200:
                # We check the connection to Serge, and we display a cross
                img_serge_creation = Image.open("imgs/error.png")
                img_serge_creation = img_serge_creation.resize((24, 32))
                label_serge_creation.image = ImageTk.PhotoImage(img_serge_creation)
                label_serge_creation['image'] = label_serge_creation.image
                newprogresswindow.update()

                error_window("Erreur lors de la création du produit : erreur lors de la requête à Serge")
                return

            if response.text == "":
                # We check the connection to Serge, and we display a cross
                img_serge_creation = Image.open("imgs/error.png")
                img_serge_creation = img_serge_creation.resize((24, 32))
                label_serge_creation.image = ImageTk.PhotoImage(img_serge_creation)
                label_serge_creation['image'] = label_serge_creation.image
                newprogresswindow.update()

                error_window("Erreur lors de la création du produit : réponse vide de Serge")
                return

            # We get the response
            response_dict = eval(response.json())

            # We get the response with only the values
            all_response = response_dict['choices'][0]['text']

            # We split the response to get all the infos
            all_infos = all_response.split("|")

            # We verify that we have all the infos
            if len(all_infos) != 4:
                # We check the connection to Serge, and we display a cross
                img_serge_creation = Image.open("imgs/error.png")
                img_serge_creation = img_serge_creation.resize((24, 32))
                label_serge_creation.image = ImageTk.PhotoImage(img_serge_creation)
                label_serge_creation['image'] = label_serge_creation.image
                newprogresswindow.update()

                error_window("Erreur lors de la création du produit : pas assez d'infos de la part de Serge")
                return

            # We create the product

            # We create the price
            price = random.randint(10, 1000)

            # Create a dictionary with all the infos
            all_infos_dict = {
                "titleEN": all_infos[0].strip(),
                "titleFR": all_infos[1].strip(),
                "descriptionEN": all_infos[2].strip(),
                "descriptionFR": all_infos[3].strip(),
                "price": price,
            }

            # We verify that we have all the infos
            if len(all_infos_dict) != 5:
                # We check the connection to Serge, and we display a cross
                img_serge_creation = Image.open("imgs/error.png")
                img_serge_creation = img_serge_creation.resize((24, 32))
                label_serge_creation.image = ImageTk.PhotoImage(img_serge_creation)
                label_serge_creation['image'] = label_serge_creation.image
                newprogresswindow.update()

                error_window(
                    "Erreur lors de la création du produit : pas assez d'infos de la part de Serge ou erreur lors de la création du dictionnaire")
                return

            # We check the connection to Serge, and we display a check
            img_serge_creation = Image.open("imgs/check.png")
            img_serge_creation = img_serge_creation.resize((24, 32))
            label_serge_creation.image = ImageTk.PhotoImage(img_serge_creation)
            label_serge_creation['image'] = label_serge_creation.image
            newprogresswindow.update()

            # We make a request to the stable diffusion API to create the images

            # We setup the JSON body

            json_body_stable_diffusion = {
                "prompt": all_infos_dict['descriptionEN'],
                "steps": 10,
                "batch_size": 4,
                "batch_count": 4
            }

            # We verify that the url does not end with a /, if it does, we remove it
            if urlstabledecoded.endswith("/"):
                real_url_stable = urlstabledecoded + "v1/txt2img"
            else:
                real_url_stable = urlstabledecoded + "/v1/txt2img"

            # We make the request

            response_stable_diffusion = requests.post(real_url_stable, json=json_body_stable_diffusion,
                                                      auth=(usernamestableapachedecoded, apachestablepassworddecoded))

            # We get the response

            if response_stable_diffusion.status_code != 200:
                # We check the connection to Stable Diffusion, and we display a cross
                img_stable_creation = Image.open("imgs/error.png")
                img_stable_creation = img_stable_creation.resize((24, 32))
                label_stable_creation.image = ImageTk.PhotoImage(img_stable_creation)
                label_stable_creation['image'] = label_stable_creation.image
                newprogresswindow.update()

                error_window("Erreur lors de la création du produit : erreur lors de la requête à Stable Diffusion")
                return

            # First we get the images in base64

            image_base64_1 = json.loads(response_stable_diffusion.text)['images'][0]
            image_base64_2 = json.loads(response_stable_diffusion.text)['images'][1]
            image_base64_3 = json.loads(response_stable_diffusion.text)['images'][2]
            image_base64_4 = json.loads(response_stable_diffusion.text)['images'][3]

            # We decode the images

            image_1 = base64.b64decode(image_base64_1)
            image_2 = base64.b64decode(image_base64_2)
            image_3 = base64.b64decode(image_base64_3)
            image_4 = base64.b64decode(image_base64_4)

            # We save the images locally in the gen_imgs folder

            title_without_spaces = all_infos_dict['titleEN'].replace(" ", "_")

            for j in range(1, 5):
                image_name = title_without_spaces + str(j) + ".jpg"
                if j == 1:
                    image = image_1
                elif j == 2:
                    image = image_2
                elif j == 3:
                    image = image_3
                elif j == 4:
                    image = image_4
                with open("gen_imgs/" + image_name, "wb") as fh:
                    fh.write(image)

            # We check the connection to Stable Diffusion, and we display a check
            img_stable_creation = Image.open("imgs/check.png")
            img_stable_creation = img_stable_creation.resize((24, 32))
            label_stable_creation.image = ImageTk.PhotoImage(img_stable_creation)
            label_stable_creation['image'] = label_stable_creation.image
            newprogresswindow.update()

            # We add the product to Prestashop

            # We create a random ean13 code
            ean13 = random.randint(1000000000000, 9999999999999)

            # If the description is longer that 400 characters, we cut it for the meta description
            if len(all_infos_dict['descriptionFR']) > 400:
                meta_description_fr = all_infos_dict['descriptionFR'][:400] + "..."
            else:
                meta_description_fr = all_infos_dict['descriptionFR']

            # We set up the product

            product = {
                "product": {
                    "id_manufacturer": 3,
                    "id_supplier": 3,
                    "new": 1,
                    "id_default_combination": 1,
                    "type": 1,
                    "ean13": ean13,
                    "state": 1,
                    "price": all_infos_dict['price'],
                    "unit_price": all_infos_dict['price'],
                    "wholesale_price": random.randint(1, 90),
                    "show_price": 1,
                    "redirect_type": "default",
                    "low_stock_threshold": 3,
                    "low_stock_alert": 1,
                    "cache_default_attribute": 0,
                    "available_for_order": 1,
                    "name": {
                        "language": {
                            "attrs": {
                                "id": "1"
                            },
                            "value": all_infos_dict['titleFR'],
                        }
                    },
                    "description": {
                        "language": {
                            "attrs": {
                                "id": "1"
                            },
                            "value": all_infos_dict['descriptionFR'],
                        }
                    },
                    "description_short": {
                        "language": {
                            "attrs": {
                                "id": "1"
                            },
                            "value": all_infos_dict['descriptionFR'],
                        },
                    },
                    "id_category_default": 33,
                    "id_tax_rules_group": 1,
                    "active": 1,
                    "id_shop_default": 1,
                    "associations": {
                        "categories": {
                            "category": [
                                {
                                    "id": 33
                                }
                            ]
                        }
                    },
                    "product_type": "standard",
                    "reference": ean13,
                    "supplier_reference": ean13,
                    "eco_tax": "0.000000",
                    "minimal_quantity": 1,
                    "meta_description": {
                        "language": {
                            "attrs": {
                                "id": "1"
                            },
                            "value": meta_description_fr,
                        }
                    },
                    "meta_keywords": {
                        "language": {
                            "attrs": {
                                "id": "1"
                            },
                            "value": all_infos_dict['titleFR'],
                        }
                    },
                    "meta_title": {
                        "language": {
                            "attrs": {
                                "id": "1"
                            },
                            "value": all_infos_dict['titleFR'],
                        }
                    },
                }
            }

            # We add the product to Prestashop

            try:
                reponse_add_product = api.create("products", product)
            except Exception as e:
                # We check the connection to Prestashop, and we display a cross
                img_prestashop_creation = Image.open("imgs/error.png")
                img_prestashop_creation = img_prestashop_creation.resize((24, 32))
                label_prestashop_creation.image = ImageTk.PhotoImage(img_prestashop_creation)
                label_prestashop_creation['image'] = label_prestashop_creation.image
                newprogresswindow.update()

                error_window("Erreur lors de la création du produit : " + str(e))
                return

            # We check the connection to Prestashop, and we display a check
            img_prestashop_creation = Image.open("imgs/check.png")
            img_prestashop_creation = img_prestashop_creation.resize((24, 32))
            label_prestashop_creation.image = ImageTk.PhotoImage(img_prestashop_creation)
            label_prestashop_creation['image'] = label_prestashop_creation.image
            newprogresswindow.update()

            # We get the id of the product

            product_id = reponse_add_product['product']['id']

            # We add the images to Prestashop

            for k in range(1, 5):
                if k == 1:
                    image_name = title_without_spaces + str(k) + ".jpg"
                    api.create_binary("images/products/" + str(product_id), file="gen_imgs/" + image_name,
                                      _type="image")
                elif k == 2:
                    image_name = title_without_spaces + str(k) + ".jpg"
                    api.create_binary("images/products/" + str(product_id), file="gen_imgs/" + image_name,
                                      _type="image")
                elif k == 3:
                    image_name = title_without_spaces + str(k) + ".jpg"
                    api.create_binary("images/products/" + str(product_id), file="gen_imgs/" + image_name,
                                      _type="image")
                elif k == 4:
                    image_name = title_without_spaces + str(k) + ".jpg"
                    api.create_binary("images/products/" + str(product_id), file="gen_imgs/" + image_name,
                                      _type="image")

            # We check the connection to Prestashop, and we display a check
            img_prestashop_images = Image.open("imgs/check.png")
            img_prestashop_images = img_prestashop_images.resize((24, 32))
            label_prestashop_images.image = ImageTk.PhotoImage(img_prestashop_images)
            label_prestashop_images['image'] = label_prestashop_images.image
            newprogresswindow.update()

            # We get the stock_available_id

            stock_available_id = reponse_add_product['product']['associations']['stock_availables'][0]['id']

            # We update the stock

            stock = {
                "stock_availables": {
                    "id": int(stock_available_id),
                    "id_product": product_id,
                    "id_product_attribute": 0,
                    "quantity": 1000,
                    "depends_on_stock": 0,
                    "id_shop": 1,
                    "out_of_stock": 2,
                }
            }

            # We update the stock
            try:
                api.write("stock_availables", stock)
            except Exception as e:
                # We check the connection to Prestashop, and we display a cross
                img_prestashop_stock = Image.open("imgs/error.png")
                img_prestashop_stock = img_prestashop_stock.resize((24, 32))
                label_prestashop_stock.image = ImageTk.PhotoImage(img_prestashop_stock)
                label_prestashop_stock['image'] = label_prestashop_stock.image
                newprogresswindow.update()

                error_window("Erreur lors de la création du produit : " + str(e))
                return

            # We check the connection to Prestashop, and we display a check
            img_prestashop_stock = Image.open("imgs/check.png")
            img_prestashop_stock = img_prestashop_stock.resize((24, 32))
            label_prestashop_stock.image = ImageTk.PhotoImage(img_prestashop_stock)
            label_prestashop_stock['image'] = label_prestashop_stock.image
            newprogresswindow.update()

            # We create the dictionary for the update of the product attributes

            update_attr_product = {
                "product": {
                    "id": product_id,
                    "cache_default_attribute": 0,
                    "price": all_infos_dict['price'],
                }
            }

            # We update the product attributes

            try:
                api.writePatch("products", update_attr_product)
            except Exception as e:
                # We check the connection to Prestashop, and we display a cross
                img_prestashop_attribute = Image.open("imgs/error.png")
                img_prestashop_attribute = img_prestashop_attribute.resize((24, 32))
                label_prestashop_attribute.image = ImageTk.PhotoImage(img_prestashop_attribute)
                label_prestashop_attribute['image'] = label_prestashop_attribute.image
                newprogresswindow.update()

                error_window("Erreur lors de la création du produit : " + str(e))
                return

            # We check the connection to Prestashop, and we display a check
            img_prestashop_attribute = Image.open("imgs/check.png")
            img_prestashop_attribute = img_prestashop_attribute.resize((24, 32))
            label_prestashop_attribute.image = ImageTk.PhotoImage(img_prestashop_attribute)
            label_prestashop_attribute['image'] = label_prestashop_attribute.image
            newprogresswindow.update()

            # We delete the chat from Serge

            url_delete = urlsergedecoded + "/chat/" + chat_id

            response_delete = requests.delete(url_delete, auth=(usernamesergeapachedecoded, apachesergepassworddecoded))

            if response_delete.status_code != 200:
                # We check the connection to Serge, and we display a cross
                img_serge_delete = Image.open("imgs/error.png")
                img_serge_delete = img_serge_delete.resize((24, 32))
                label_serge_delete.image = ImageTk.PhotoImage(img_serge_delete)
                label_serge_delete['image'] = label_serge_delete.image
                newprogresswindow.update()

                error_window("Erreur lors de la création du produit : erreur lors de la requête à Serge")
                return

            # We check the connection to Serge, and we display a check
            img_serge_delete = Image.open("imgs/check.png")
            img_serge_delete = img_serge_delete.resize((24, 32))
            label_serge_delete.image = ImageTk.PhotoImage(img_serge_delete)
            label_serge_delete['image'] = label_serge_delete.image
            newprogresswindow.update()

            # We add to the progress bar
            progressbar['value'] += 100 / int(scale_value.get())
            newprogresswindow.update()

            # if the value of the progress bar is not 100, we reset the images to the loading image
            if progressbar['value'] != 100:
                # We reset the images to the loading image
                img_serge_creation = Image.open("imgs/loading.png")
                img_serge_creation = img_serge_creation.resize((24, 32))
                label_serge_creation.image = ImageTk.PhotoImage(img_serge_creation)
                label_serge_creation['image'] = label_serge_creation.image
                img_stable_creation = Image.open("imgs/loading.png")
                img_stable_creation = img_stable_creation.resize((24, 32))
                label_stable_creation.image = ImageTk.PhotoImage(img_stable_creation)
                label_stable_creation['image'] = label_stable_creation.image
                img_prestashop_creation = Image.open("imgs/loading.png")
                img_prestashop_creation = img_prestashop_creation.resize((24, 32))
                label_prestashop_creation.image = ImageTk.PhotoImage(img_prestashop_creation)
                label_prestashop_creation['image'] = label_prestashop_creation.image
                img_prestashop_images = Image.open("imgs/loading.png")
                img_prestashop_images = img_prestashop_images.resize((24, 32))
                label_prestashop_images.image = ImageTk.PhotoImage(img_prestashop_images)
                label_prestashop_images['image'] = label_prestashop_images.image
                img_prestashop_stock = Image.open("imgs/loading.png")
                img_prestashop_stock = img_prestashop_stock.resize((24, 32))
                label_prestashop_stock.image = ImageTk.PhotoImage(img_prestashop_stock)
                label_prestashop_stock['image'] = label_prestashop_stock.image
                img_prestashop_attribute = Image.open("imgs/loading.png")
                img_prestashop_attribute = img_prestashop_attribute.resize((24, 32))
                label_prestashop_attribute.image = ImageTk.PhotoImage(img_prestashop_attribute)
                label_prestashop_attribute['image'] = label_prestashop_attribute.image
                img_serge_delete = Image.open("imgs/loading.png")
                img_serge_delete = img_serge_delete.resize((24, 32))
                label_serge_delete.image = ImageTk.PhotoImage(img_serge_delete)
                label_serge_delete['image'] = label_serge_delete.image
                newprogresswindow.update()

        # We display a window to inform the user that the products have been created using the tkinter module

        newproductwindow = Toplevel(root)
        newproductwindow.title("Produits crées")
        newproductwindow.geometry("600x200")

        # Open the image
        img_check = Image.open("imgs/check.png")
        # Resize the image
        img_check = img_check.resize((32, 32))
        # Create a group to store the image, the text and the button
        group_check = ttk.Frame(newproductwindow)
        # Create a group to store the image and the text
        group_txt_check = ttk.Frame(group_check)
        # Add the image
        label_check = ttk.Label(group_txt_check)
        label_check.image = ImageTk.PhotoImage(img_check)
        label_check['image'] = label_check.image
        label_check.grid(column=0, row=0)
        # Add the text
        Label(group_txt_check,
              text="Les produits ont été crées avec succès", font=('Arial', 16)).grid(column=1, row=0)
        group_txt_check.grid(column=0, row=0)
        # Add the button
        ttk.Button(group_check, text="OK", command=newproductwindow.destroy).grid(column=0, row=1)
        group_check.grid(column=0, row=0)
        # Place the group check in the center of the window
        group_check.place(relx=0.5, rely=0.5, anchor="center")


# Function to verify that the user wants to create the products


def verify_create_btn():
    # Open a window to verify that the user wants to create the products
    newverifywindow = Toplevel(root)
    newverifywindow.title("Vérification")
    newverifywindow.geometry("600x300")
    group_verify = ttk.Frame(newverifywindow)
    group_txt_warning = ttk.Frame(group_verify)
    # Add the warning image
    warning_img = Image.open("imgs/warning.png")
    warning_img = warning_img.resize((32, 32))
    label_warning = ttk.Label(group_txt_warning)
    label_warning.image = ImageTk.PhotoImage(warning_img)
    label_warning['image'] = label_warning.image
    label_warning.grid(column=0, row=0)
    Label(group_txt_warning,
          text="Voulez-vous vraiment créer les produits ?", font=('Arial', 16)).grid(column=1, row=0)
    group_txt_warning.grid(column=0, row=0)
    Label(group_verify, text="", width=10).grid(column=0, row=1)
    group_button = ttk.Frame(group_verify)
    ttk.Button(group_button, text="Oui", command=lambda: create_products(newverifywindow)).grid(column=0, row=0)
    # Blank space (Taylor's version)
    ttk.Label(group_button, text="", width=10).grid(column=1, row=0)
    ttk.Button(group_button, text="Non", command=newverifywindow.destroy).grid(column=2, row=0)

    group_button.grid(column=0, row=2)
    group_verify.grid(column=0, row=0)
    # Place the group verify in the center of the window
    group_verify.place(relx=0.5, rely=0.5, anchor="center")


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("AI Lasagne Generator 3000")
photo = PhotoImage(file="imgs/retrorococo.png")
root.iconphoto(False, photo)

# Open the image
img = Image.open("imgs/retrorococo.png")
# Resize the image
img = img.resize((64, 64))
# Convert the image to PhotoImage
photoApp = ImageTk.PhotoImage(img)

# Add the icon of the application on the center of the window
ttk.Label(frm, image=photoApp).grid(column=0, row=1)

ttk.Label(frm, text="Bienvenue sur le générateur de produit Prestashop AI Lasagne Generator 3000",
          font=('Arial', 16)).grid(column=0, row=0)
ttk.Button(frm, text="Options", command=optionwindow).grid(column=1, row=0)


def vnumcmd(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        # Display a warning message under the slider
        ttk.Label(frm, text="Veuillez entrer un nombre valide", foreground="red", font=('Arial', 12)).grid(column=0,
                                                                                                           row=5)
        return False


vcmd = (root.register(vnumcmd), '%P')
ttk.Label(frm, text="Créations des produits", font=('Arial', 12)).grid(column=0, row=2)
# Create an Entry widget for the text field
scale_value = StringVar()
scale_value_entry = Entry(frm, textvariable=scale_value, validate="all", validatecommand=vcmd)
scale_value_entry.grid(sticky="w", column=1, row=4)

ttk.Button(frm, text="Obtenir le dernier produit crée", command=get_last_product).grid(column=0, row=6)

# Blank space (Taylor's version)
ttk.Label(frm, text="").grid(column=0, row=9)

# We create a group to store the two text fields if the user wants to specified a category or a specific product (the two can't be specified at the same time)

group_category = ttk.Frame(frm)

# Create a LabelFrame for the group
group_category = ttk.LabelFrame(frm, text="Catégorie ou produit spécifique \n(un seul des deux peut être spécifié)")

# Create a Label to display the text field in bold in the two columns
ttk.Label(group_category, text="ATTENTION : Entrez un mot en anglais", font=('Arial-BoldMT', 12)).grid(column=0, row=0, columnspan=2)

# Create a StringVar to store the value of the category
category_value = StringVar()
# Create a Label to display the text field
ttk.Label(group_category, text="Catégorie :").grid(column=0, row=1)
# Create an Entry widget for the text field
category_value_entry = Entry(group_category, textvariable=category_value)
category_value_entry.grid(column=1, row=1)

# Create a StringVar to store the value of the product
product_value = StringVar()
# Create a Label to display the text field
ttk.Label(group_category, text="Produit :").grid(column=0, row=2)
# Create an Entry widget for the text field
product_value_entry = Entry(group_category, textvariable=product_value)
product_value_entry.grid(column=1, row=2)

# Define a function that disable the text field of the category if the user wants to specify a product and vice versa


def disable_category(*args):
    if category_value.get() != "":
        product_value_entry.config(state="disabled")
    elif product_value.get() != "":
        category_value_entry.config(state="disabled")
    elif category_value.get() == "" and product_value.get() == "":
        category_value_entry.config(state="normal")
        product_value_entry.config(state="normal")

# Bind this function to the Entry widget
category_value.trace("w", disable_category)

# Set this function to the command parameter of the Entry widge
product_value.trace("w", disable_category)

# Add the group to the window

group_category.grid(column=0, row=10)

# Blank space (Taylor's version)
ttk.Label(frm, text="").grid(column=0, row=11)

# Add a button to create the products

ttk.Button(frm, text="Créer les produits", command=verify_create_btn).grid(column=0, row=12)


# Define a function that will update the text field with the current value of the scale


def update_scale_value(val):
    scale_value.set(val)


# Define a function that will update the scale with the current value of the entry field
def update_scale_from_entry(*args):
    try:
        numberofproducts.set(int(scale_value.get()))
    except ValueError:
        pass


# Bind this function to the Entry widget
scale_value.trace("w", update_scale_from_entry)

# Set this function as the command parameter of the Scale widget
numberofproducts = Scale(frm, from_=1, to=100, orient=HORIZONTAL, command=update_scale_value)
numberofproducts.grid(column=0, row=4)

root.mainloop()
