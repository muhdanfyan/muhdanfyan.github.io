    <!-- start page title -->
    <div class="row">
        <div class="col-12">
            <div class="page-title-box">
                <div class="page-title-right">
                    <ol class="breadcrumb m-0">
                        <li class="breadcrumb-item"><a href="javascript: void(0);">UBold</a></li>
                        <li class="breadcrumb-item"><a href="javascript: void(0);">eCommerce</a></li>
                        <li class="breadcrumb-item active">Products</li>
                    </ol>
                </div>
                <h4 class="page-title">Products</h4>
            </div>
        </div>
    </div>     
    <!-- end page title --> 

    <div class="row">
        <div class="col-12">
            <div class="card-box">
                <div class="row">
                    <div class="col-lg-8">
                        <form class="form-inline">
                            <div class="form-group">
                                <label for="inputPassword2" class="sr-only">Search</label>
                                <input type="search" class="form-control" id="inputPassword2" placeholder="Search...">
                            </div>
                            <div class="form-group mx-sm-3">
                                <label for="status-select" class="mr-2">Sort By</label>
                                <select class="custom-select" id="status-select">
                                    <option selected="">All</option>
                                    <option value="1">Popular</option>
                                    <option value="2">Price Low</option>
                                    <option value="3">Price High</option>
                                    <option value="4">Sold Out</option>
                                </select>
                            </div>
                        </form>
                    </div>
                    <div class="col-lg-4">
                        <div class="text-lg-right mt-3 mt-lg-0">
                            <button type="button" class="btn btn-success waves-effect waves-light mr-1"><i class="mdi mdi-settings"></i></button>
                            <!-- <a href="<?= base_url('product/input') ?>" class="btn btn-danger waves-effect waves-light"><i class="mdi mdi-plus-circle mr-1"></i> Add New</a> -->
                            <button type="button" class="btn btn-danger waves-effect waves-light" data-toggle="modal" data-target="#con-close-modal"><i class="mdi mdi-plus-circle mr-1"></i> Add New</button>
                        </div>
                    </div><!-- end col-->
                </div> <!-- end row -->
            </div> <!-- end card-box -->
        </div> <!-- end col-->
    </div>
    <!-- end row-->

    <div class="row">
    <?php
        if ($dataproduk->num_rows() > 0){

            foreach ($dataproduk->result_array() as $row) {
                # code...
            ?>
            <div class="col-md-6 col-xl-3">
                <div class="card-box product-box">

                    <div class="product-action">
                        <a href="<?= base_url() ?>product/detail_edit/<?= $row['id_produk'] ?>" class="btn btn-primary btn-xs waves-effect waves-light"><i class="mdi mdi-format-columns"></i></a>
                        <a href="<?= base_url() ?>product/input" class="btn btn-success btn-xs waves-effect waves-light"><i class="mdi mdi-pencil"></i></a>
                        <a href="<?= base_url() ?>product/delete/<?= $row['id_produk'] ?>" class="btn btn-danger btn-xs waves-effect waves-light"><i class="mdi mdi-close"></i></a>
                    </div>

                    <div>
                        <img src="<?= base_url() ?>/assets/uploads/files/<?= $row['file_gambar'] ?>" alt="product-pic" class="img-fluid" height="300px">
                    </div>

                    <div class="product-info">
                        <div class="row align-items-center">
                            <div class="col">
                                <h5 class="font-16 mt-0 sp-line-1"><a href="ecommerce-prduct-detail.html" class="text-dark"><?= $row['nama_produk'] ?></a> </h5>
                                <div class="text-warning mb-2 font-13">
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                    <i class="fa fa-star"></i>
                                </div>
                                <h5 class="m-0"> <span class="text-muted"> Stocks : <?= $row['stok'] ?></span></h5>
                            </div>
                            <div class="col-auto">
                                <div class="product-price-tag">
                                    $49
                                </div>
                            </div>
                        </div> <!-- end row -->
                    </div> <!-- end product info-->
                </div> <!-- end card-box-->
            </div> <!-- end col-->
        <?php
            }
        }
    ?>
    </div>
    <!-- end row-->

    <div class="row">
        <div class="col-12">
            <ul class="pagination pagination-rounded justify-content-end mb-3">
                <li class="page-item">
                    <a class="page-link" href="javascript: void(0);" aria-label="Previous">
                        <span aria-hidden="true">«</span>
                        <span class="sr-only">Previous</span>
                    </a>
                </li>
                <li class="page-item active"><a class="page-link" href="javascript: void(0);">1</a></li>
                <li class="page-item"><a class="page-link" href="javascript: void(0);">2</a></li>
                <li class="page-item"><a class="page-link" href="javascript: void(0);">3</a></li>
                <li class="page-item"><a class="page-link" href="javascript: void(0);">4</a></li>
                <li class="page-item"><a class="page-link" href="javascript: void(0);">5</a></li>
                <li class="page-item">
                    <a class="page-link" href="javascript: void(0);" aria-label="Next">
                        <span aria-hidden="true">»</span>
                        <span class="sr-only">Next</span>
                    </a>
                </li>
            </ul>
        </div> <!-- end col-->
    </div>
    <!-- end row-->
    
    <!-- Modal  -->
    <div id="con-close-modal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" style="padding-right: 17px;" aria-modal="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">Modal Content is Responsive</h4>
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                </div>
                <div class="modal-body p-4">
                    <form action="<?= base_url('product/insert') ?>" method="post" enctype="multipart/form-data">
                        <div class="form-group mb-3">
                            <label for="product-name">Nama Produk <span class="text-danger">*</span></label>
                            <input type="text" id="nama_produk" name="nama_produk" class="form-control" placeholder="Cth : Handphone, dlln.">
                        </div>

                        <div class="row">
                            <div class="col-sm-6">
                                <div class="form-group mb-3">
                                    <label class="mb-2">Status Barang <span class="text-danger">*</span></label>
                                    <br/>
                                    <div class="radio form-check-inline">
                                        <input type="radio" id="inlineRadio1" value="Tersedia" name="stok" checked="">
                                        <label for="inlineRadio1"> Tersedia </label>
                                    </div>
                                    <div class="radio form-check-inline">
                                        <input type="radio" id="inlineRadio2" value="Habis" name="stok">
                                        <label for="inlineRadio2"> Habis </label>
                                    </div>
                                </div>
                            
                            </div>
                            <div class="col-sm-6">        
                                <div class="form-group mb-3">
                                    <label for="product-reference">Berat <span class="text-danger">*</span></label>
                                    <input type="text" id="berat" name="berat" class="form-control" placeholder="Berat Satuan Kilogram">
                                </div>
                            </div>
                        </div>


                        <div class="row">
                            <div class="col-sm-4">
                                <div class="form-group mb-3">
                                    <label for="harga_modal">Harga Modal <span class="text-danger">*</span></label>
                                    <input type="number" class="form-control" id="harga_modal" name="harga_modal" placeholder="Harga Modal">
                                </div>
                            </div>
                            <div class="col-sm-4">
                                <div class="form-group mb-3">
                                    <label for="harga_produk">Harga Produk <span class="text-danger">*</span></label>
                                    <input type="number" class="form-control" id="harga_produk" name="harga_produk" placeholder="Harga Produk">
                                </div>
                            </div>
                            <div class="col-sm-4">
                                <div class="form-group mb-3">
                                <label for="harga_coret">Harga Coret <span class="text-danger">*</span></label>
                                <input type="number" class="form-control" id="harga_coret" name="harga_coret" placeholder="Harga Produk">
                            </div>
                            </div>
                        </div>

                        <div class="form-group mb-3">
                            <label for="kategori">Kategori <span class="text-danger">*</span></label>
                            <select class="form-control select2" id="kategori" name="kategori" style>
                                <option width='1000px'>Pilih Kategori</option>
                                <?php
                                    if ($kategori->num_rows() > 0){
                                        foreach($kategori->result_array() as $row){
                                ?>
                                    <option value="<?= $row['id_kategori'] ?>"><?= $row['nama_kategori'] ?></option>
                                <?php                 
                                        }
                                    }  
                                ?>

                            </select>
                        </div>
                        <div class="form-group mb-3">
                            <label for="harga_coret">File Gambar (rasio 1x1 minimal 1mb) <span class="text-danger">*</span></label>
                            <input type="file" class="form-control" id="file_gambar" name="file_gambar">
                        </div>
                        <div class="form-group mb-3">
                            <label for="deskripsi">Deskripsi <span class="text-danger">*</span></label>
                            <textarea class="form-control" id="deskripsi"  name="deskripsi" rows="5" placeholder="Please enter description"></textarea>
                        </div>

                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary waves-effect" data-dismiss="modal">Close</button>
                            <button type="submit" class="btn btn-info waves-effect waves-light">Save changes</button>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    </div>
