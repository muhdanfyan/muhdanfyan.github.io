<?php
    include_once ("include/koneksi.php");
    $page = $_GET['page'];
    if (empty($page))
        $page=0;
    $limit = 10;

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Valuz.id - Pusat Barang-barang Bagus</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">

</head>
<body>
    <div class="wrap">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8 col-md-10 col-sm-12 badan">
                    <div class="slide-show">
                        <div id="carouselId" class="carousel slide" data-ride="carousel">
                            <ol class="carousel-indicators">
                            <?php
                                $sqlSlide = "SELECT * FROM slide";
                                $resultSlide = $conn->query($sqlSlide);
                                
                                if ($resultSlide->num_rows > 0) {
                                    // output data of each row
                                    $active = "active";
                                    for ($i=0;$i<$resultSlide->num_rows; $i++){?>
                                        <li data-target="#carouselId" data-slide-to="<?= $i ?>" class="<?= $active ?>"></li>
                                <?php $active =""; } ?>
                            </ol>
                            <div class="carousel-inner" role="listbox">
                                <?php
                                $active = " active";
                                while($slide = $resultSlide->fetch_assoc()) {
                                ?>
                                <div class="carousel-item<?= $active ?>">
                                    <img src="https://valuz.id/admin/assets/uploads/files/<?= $slide['file_slide'] ?>" data-src="holder.js/900x500/auto/#777:#555/text:First slide" alt="First slide" width="100%">
                                    <div class="carousel-caption d-none d-md-block">
                                        <!-- <h3>Title</h3>
                                        <p>Description</p> -->
                                    </div>
                                </div>
                            <?php
                                $active = "";
                                }
                            }
                            ?>
                            </div>
                            <a class="carousel-control-prev" href="#carouselId" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                            </a>
                            <a class="carousel-control-next" href="#carouselId" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                            </a>
                        </div>
                    </div>
                    <div class="home-catalog-produk">

                        <div class="row">
                            <div class="col-lg-12 text-center">
                                <h3>PUSAT BARANG BAGUS</h3>
                            </div>

                            <?php
                                    $num_page = floor($conn->query("SELECT * FROM produk")->num_rows / $limit);
                                    $offset = $page * $limit;
                                    $sql = "SELECT * FROM produk limit $limit offset $offset";
                                    $result = $conn->query($sql);

                                if ($result->num_rows > 0) {
                                    // output data of each row
                                    while($row = $result->fetch_assoc()) {
                                        ?>
                                            
                                        <div class="col-lg-6 col-sm-12 text-center">
                                            <div class="catalog-produk">
                                                <div class="image-catalog">
                                                    <a href="#"><img src="https://valuz.id/admin/assets/uploads/files/<?= $row['file_gambar'] ?>" alt="" width="80%"></a>
                                                </div>
                                                <div class="info-catalog">
                                                    <div class="nama-produk">
                                                        <?= $row['nama_produk'] ?>
                                                    </div>
                                                    <div class="harga-produk">
                                                        Rp. <?= number_format($row['harga_produk'],0,',','.'); ?> <s><?= number_format($row['harga_coret'],0,',','.'); ?></s>
                                                    </div>
                                                    <div class="link-detail">
                                                        <a href="detail.php?id=<?= $row['id_produk'] ?>" class="btn btn-primary"><i class="fa fa-info-circle" aria-hidden="true"></i> Detail</a>
                                                    </div>
                                                </div>
                                            </div> 
                                        </div>
                                        <?php
                                    }
                                } else {
                                    echo "0 results";
                                }
                            ?>
                        </div>
                    </div>
                    <nav aria-label="Page navigation">
                      <ul class="pagination justify-content-center">
                        <li class="page-item disabled">
                          <a class="page-link" href="#" aria-label="Previous">
                            <span aria-hidden="true">&laquo;</span>
                            <span class="sr-only">Previous</span>
                          </a>
                        </li>
                        <?php
                            for ($i=0;$i<=$num_page; $i++){
                                if ($page==$i)
                                    $active = " active";
                                else
                                    $active = "";
                                ?>
                                    <li class="page-item<?= $active ?>"><a class="page-link" href="?page=<?= $i ?>"><?= $i+1 ?></a></li>
                                <?php
                            }
                        ?>
                        <li class="page-item">
                          <a class="page-link" href="#" aria-label="Next">
                            <span aria-hidden="true">&raquo;</span>
                            <span class="sr-only">Next</span>
                          </a>
                        </li>
                      </ul>
                    </nav>
                    <footer class="footer text-center">
                        <div class="container">
                            Powered <a href="https://valuz.id">valuz.id</a> 2020
                        </div>
                    </footer>
                </div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>