# Basic centralized link publishing system (FDLA WS24/25)

## Overview

This web application allows users to submit links, which are stored in a database and made available through an ATOM feed. Users can enter their name, the URL of a game, and a description, and these submissions are displayed in a feed format, allowing for easy access and subscription.

## Features

User Submission Form: Users can enter their name, a game link, and a description.
Database Storage: Submissions are stored in a SQLite database.
ATOM Feed: Provides an ATOM feed containing all submitted links, accessible via a specific URL.
Responsive Design: The application features a clean interface with a dark theme.

## Technologies Used

Flask: Python web framework for building the application.
Flask-SQLAlchemy: ORM for database interactions.
SQLite: Lightweight database for storing submissions.
HTML/CSS: For front-end design.

## Authors: 
- Lea Kassandra Krumbach (lkrumba2) 
- Norma Katrin Wilcken (nwilcken)