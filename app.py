from flask import Flask, request, render_template
import sqlite3


con = sqlite3.connect("weather_database.db")