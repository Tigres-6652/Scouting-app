print('hola')
import pyodbc
import base64

# Configuración de la conexión a la base de datos
def get_db_connection():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost\\SQLEXPRESS;'
                          'Database=imagen;'  # Cambia el nombre a tu base de datos
                          'Trusted_Connection=yes;')
    return conn

@app.route('/images')
def images():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Id, Name FROM Images')
    images = cursor.fetchall()
    conn.close()
    return render_template('images.html', images=images)

@app.route('/image/<int:image_id>')
def image(image_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT Data FROM Images WHERE Id = ?', (image_id,))
    image_data = cursor.fetchone()
    conn.close()
    
    if image_data and image_data[0]:
        return Response(image_data[0], mimetype='image/png')  # Cambia 'image/png' según el formato real
    return "Image not found", 404
@app.route('/save_drawn_image', methods=['POST'])
def save_drawn_image():
    try:
        # Obtener datos de la imagen del cuerpo de la solicitud
        data = request.json['image']
        image_data = base64.b64decode(data.split(',')[1])  # Decodificar la imagen

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insertar la imagen en la base de datos
        cursor.execute('''
            INSERT INTO Images (Data, Name) VALUES (?, ?)
        ''', (pyodbc.Binary(image_data), "Dibujo Personalizado"))  # Puedes cambiar el nombre si lo deseas

        conn.commit()  # Hacer commit de la transacción
        conn.close()

        return jsonify({"status": "success"})
    except Exception as e:
        print(f"Error saving image: {e}")  # Imprimir el error en la consola
        return jsonify({"status": "error", "message": str(e)}), 500