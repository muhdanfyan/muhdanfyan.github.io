<?php
    include_once("include/koneksi.php");
    $ip = IPnya();
    // $produk = 7;

    $nama = $_GET['name'];
    $produk = $_GET['produk'];
    $wa = intval($_GET['whatsapp']);
    
    if (isset($nama) && isset($wa)){
        // $url = "https://valuz.id/form.php?name=".  str_replace(" ", "+", $nama) ."&whatsapp=0" . $wa ;
        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);

        $sql2 = "SELECT * FROM `tbl_wa` WHERE produk=$produk AND telepon=$wa" ;
        $result2 = $conn->query($sql2);

        $sql3 = "SELECT * FROM `produk` WHERE id_produk=$produk" ;
        $result3 = $conn->query($sql3);
        $data = $result3->fetch_assoc();
        
        $biaya = $data['harga_produk'];
        
        $a=true;
        if ($result2->num_rows == 0){
        
        $sql = "INSERT INTO `tbl_wa` (`nama_kontak`, `telepon`, `ip`,  `produk`) 
        VALUES ('$nama', '$wa', '$ip', '$produk');";

        if ($conn->query($sql) === TRUE) {
            $linkid = $conn->insert_id;
            $a=true;
            
            } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
            $a = false;
            }
        $phone = '62' . $wa;
        $message = 'Halo, *'. $nama .'*

Dengan saya CS *[Nama CS]* :

Kami sudah terima pesanannya  untuk produk *'. $data['nama_produk'] .'*

Tolong isi alamatnya dengan lengkap :

Nama :
Alamat Lengkap (RT/RW) : 
Desa/Kelurahan: 
Kecamatan: 
Kota/Kab: 
Provinsi: 
Kode Pos:

Jumlah Produk yang Anda pesan :

Mohon segera dikonfirmasi ya *'. $nama .'* untuk pesanannya. 

*TERIMA KASIH*';

        if (($a) && sendwanotif($message, $phone, "Pesan Barang $produk"))
            header("Location: thanks.php?nama=$nama&wa=0$wa");
        else{
            echo $conn->error;   
            echo $konek->error;
            }
        }
            echo "<script>alert('Nomor sudah pernah didaftarkan untuk kelas ini');history.go(-1);</script>";
    }
?>