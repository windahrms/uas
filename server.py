from flask import Flask, request, jsonify
from buku_kontak import BukuKontak

app = Flask(__name__)
buku = BukuKontak()

# Contoh data awal
buku.tambah_kontak(Kontak("Andi", "0812345678"))
buku.tambah_kontak(Kontak("Budi", "0876543210"))

@app.route('/kontak', methods=['GET', 'POST'])
def manage_kontak():
    if request.method == 'POST':  # CREATE
        data = request.json
        if buku.tambah_kontak(Kontak(data['nama'], data['telepon'])):
            return jsonify({"status": "success"}), 201
        return jsonify({"status": "duplicate"}), 400
    
    elif request.method == 'GET':  # READ
        return jsonify([{"nama": k.nama, "telepon": k.telepon} for k in buku.daftar_kontak])

@app.route('/kontak/<nama>', methods=['DELETE', 'PUT'])
def kontak_detail(nama):
    if request.method == 'DELETE':  # DELETE
        if buku.hapus_kontak(nama):
            return jsonify({"status": "deleted"})
        return jsonify({"status": "not found"}), 404
    
    elif request.method == 'PUT':  # UPDATE
        data = request.json
        if buku.hapus_kontak(nama):
            buku.tambah_kontak(Kontak(data['nama'], data['telepon']))
            return jsonify({"status": "updated"})
        return jsonify({"status": "update failed"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)