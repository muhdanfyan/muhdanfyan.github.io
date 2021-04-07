<?php
    include_once ("include/koneksi.php");

    $id= $_GET['id'];
    $sql = "SELECT * FROM produk where id_produk='$id'";
    $result = $conn->query($sql);
    // output data of each row
    $row = $result->fetch_assoc(); // Nilai Proses
    $kode = sprintf("%05d", $id);
    $harga_produk = $row['harga_produk'];
    $harga_coret = $row['harga_coret'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $row['nama_produk'] ?></title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">

</head>
<body>
    <div class="wrap">
        <div class="container">
            <div class="row justify-content-center">
                
                <div class="col-lg-8 col-md-10 col-sm-12 badan">
                    <div class="home-catalog-produk">

                        <div class="row">
                            <div class="col-lg-12">
                                <div class="head-produk">
                                    <div class="head-title text-center">
                                        <h3><?= $row['nama_produk'] ?></h3>
                                    </div>
                                    <div class="img-produk text-center">
                                        <img src="https://valuz.id/admin/assets/uploads/files/<?= $row['file_gambar'] ?>" alt="" width='300px'>
                                        <div class="slider">

                                        </div>
                                    </div>
                                    <div class="info-produk">
                                        <div class="row justify-content-center">
                                            <div class="col-md-6 col-sm-12">
                                               
                                                <table class="table table-striped" width="100%">
                                                        <tbody>
                                                            <tr>
                                                                <td>Kode </td>
                                                                <td>AG<?= $kode ?></td>
                                                            </tr>
                                                            <tr>
                                                                <td>Harga</td>
                                                                <td>Rp. <?= number_format($harga_produk,0,',','.'); ?> <s><?= number_format($harga_coret,0,',','.'); ?></s></td>
                                                            </tr>
                                                        </tbody>
                                                </table>
                                            </div>
                                            <div class="col-md-6 col-sm-12">
                                                <table class="table table-striped table-inverse" width="100%">
                                                        <tbody>
                                                            <tr>
                                                                <td>Stok </td>
                                                                <td>Ready</td>
                                                            </tr>
                                                            <tr>
                                                                <td>Berat(/pcs)</td>
                                                                <td><?= $row['berat'] ?>Kg</s></td>
                                                            </tr>
                                                        </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="detail-produk">
                                    <div class="head-detail text-center">
                                        <h2>Detail Produk</h2>
                                    </div>
                                    <div class="isi-detail-produk">
                                    <?php
                                        $sql = "SELECT * FROM gambar where produk='$id' ORDER BY urutan";
                                        $result = $conn->query($sql);

                                        while($row = $result->fetch_assoc()){
                                    ?>
                                        <div class="atas">
                                            <?= $row['teks_atas'] ?>
                                        </div>
                                        <div class="image-produk">
                                            <img src="https://valuz.id/admin/assets/uploads/files/<?= $row['file_gambar'] ?>" alt="">
                                        </div>
                                        <div class="bawah">
                                            <?= $row['teks_bawah'] ?>
                                        </div>
                                        <hr>
                                    <?php
                                        }
                                    ?>
                                    </div>
                                </div>
                                
                                <div class="transaksi text-center sesi">
                                    <hr>
                                    <h2 style="color:red">HATI-HATI !!!</h2>
                                    <H2>BANYAK YANG MENAWARKAN PRODUK PALSU DENGAN HARGA MURAH</H2>
                                    <img src="images/alert.png" alt="" width="200px">
                                    <hr>
                                    
                                    <h4>CARA MENDAPATKAN PRODUK INI</h4>
                                    <p><b>Sangat Mudah</b> untuk Anda bisa memiliki produk ini, dengan hanya mengklik tombol ”<b>BELI SEKARANG</b>” yang ada dibawah maka secara otomatis tim admin kami menghubungi Anda Via Whatsapp. Dan silahkan lakukan transaksi</p>
                                    
                                    <hr>
                                </div>

                                <div class="price sesi text-center">
                                    <h4 style="color:red">PROMO</h4>
                                    <H5>KHUSUS HARI INI SAJA !!!</H5>
                                    <h6>Harga Asli <s>Rp. <?= number_format($harga_coret,0,',','.'); ?></s></h6>
                                    <p>Anda Cukup Bayar</p>
                                    <h5><b>Rp. <?= number_format($harga_produk, 0, ',', '.'); ?></b></h5>
                                    <hr>
                                </div>

                                <div class="countdown text-center">
                                    <h5>BARANGNYA SISA &lt;5  STOK TERSEDIA </h5>
                                    <ul>
                                        <li><span id="days"></span>days</li>
                                        <li><span id="hours"></span>Hours</li>
                                        <li><span id="minutes"></span>Minutes</li>
                                        <li><span id="seconds"></span>Seconds</li>
                                    </ul>
                                    <!-- <div class="progress" id="progress">
                                        <div class="progress-bar bg-primary" role="progressbar" style="width: 100%;"
                                            aria-valuenow="1" aria-valuemin="0" aria-valuemax="24">Description</div>
                                    </div> -->
                                    <hr>
                                </div>

                                <div class="daftar">
                                    <form action="input.php" method="post">
                                        <h5>Isi data Anda dan dapatkan Barangnya</h5>
                                        ⬇
                                        <div class="form-group">
                                          <label for="Nama"></label>
                                          <input type="text" class="form-control" name="name" id="name" aria-describedby="helpId" placeholder="Masukkan Nama" required>
                                          <!-- <small id="helpId" class="form-text text-muted">Help text</small> -->
                                          <div class="form-group">
                                            <label for="Whatsapp"></label>
                                            <input type="number" class="form-control" name="" id="" aria-describedby="helpId" placeholder="Whatsapp (08xxxxxx)" required>
                                            <button type="submit" class="btn btn-primary">BELI SEKARANG</button>
                                            <small id="helpId" class="form-text text-muted text-left">* Pastikan Nomor Whatsapp Anda Benar dan Aktif</small>
                                            <small id="helpId" class="form-text text-muted text-left">** Penawaran ini terbatas dan harganya bisa berubah kapan saja</small>
                                            <small id="helpId" class="form-text text-muted text-left">*** Harga belum termaksud ongkos kirim dan fee adamin jika COD</small>
                                            <small id="helpId" class="form-text text-muted text-left">** Tim admin kami langsung menghubungi Anda setelah Anda mengklik tombol BELI SEKARANG</small>
                                          </div>
                                        </div>
                                    </form>
                                </div>

                                <footer class="footer text-center">
                                    <div class="container">
                                        Powered <a href="https://valuz.id">valuz.id</a> 2020
                                    </div>
                                </footer>
                            </div>

                        </div>
                    </div>
                    
                </div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script>
        const second = 1000,
        minute = second * 60,
        hour = minute * 60,
        day = hour * 24;

    let countDown = new Date('<?= date('M')?> <?= date('d')?>, <?= date('Y')?> 23:00:00').getTime(),
        x = setInterval(function() {    

        let now = new Date().getTime(),
            distance = countDown - now;

            // document.getElementById('days').innerText = Math.floor(distance / (day)),
            // document.getElementById('hours').innerText = Math.floor((distance % (day)) / (hour)),
            // document.getElementById('minutes').innerText = Math.floor((distance % (hour)) / (minute)),
            // document.getElementById('seconds').innerText = Math.floor((distance % (minute)) / second);

            document.getElementById('days').innerText = Math.floor(distance / (day)),
            document.getElementById('hours').innerText = Math.floor((distance % (day)) / (hour)),
            document.getElementById('minutes').innerText = Math.floor((distance % (hour)) / (minute)),
            document.getElementById('seconds').innerText = Math.floor((distance % (minute)) / second);

            // // $('#days').text(Math.floor(distance / (day)));
            // // $('#hours').text(Math.floor((distance % (day)) / (hour)));
            // $('#minutes').text(Math.floor(Math.floor((distance % (hour)) / (minute)));
            

            
        //do something later when date is reached
        //if (distance < 0) {
        //  clearInterval(x);
        //  'IT'S MY BIRTHDAY!;
        //}

        }, second);
    </script>
</body>
</html>