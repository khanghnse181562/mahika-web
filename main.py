from app import create_app

# Create application instance for deployment
application = create_app()
app = application

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)