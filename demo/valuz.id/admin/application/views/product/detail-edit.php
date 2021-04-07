<div class="row">
    <div class="col-12">
        <div class="page-title-box">
            <div class="page-title-right">
                <ol class="breadcrumb m-0">
                    <li class="breadcrumb-item"><a href="javascript: void(0);">UBold</a></li>
                    <li class="breadcrumb-item"><a href="javascript: void(0);">UI</a></li>
                    <li class="breadcrumb-item active">Tabs &amp; Accordions</li>
                </ol>
            </div>
            <h4 class="page-title">Product Detail</h4>
        </div>
    </div>
</div>
                <?php
                    if ($dataproduk->num_rows() > 0)
                    {
                        
                        foreach ($dataproduk->result_array() as $row)
                        {
                            
                ?>
<form action="<?= base_url('product/update/' . $id_produk) ?>" method="post">
<div class="row">
    <div class="col-xl-12">
        <div class="card-box">
            <h4 class="header-title mb-4">
                <div class="row">
                    <div class="col-sm-6" style="display:flex">Produk Detail </div>
                    <div class="col-sm-6 justify-content-end text-right">
                        <div class="btn-save">
                            <button type="submit" id="submit" class="btn btn-success btn-lg"><i class="mdi mdi-content-save-edit-outline"></i></button>
                            <a name="kembali" id="kembali" class="btn btn-danger" href="<?= base_url('product')?>"><i class="mdi mdi-keyboard-return"></i></a>
                        </div>
                    </div>
                </div>
            </h4>
            <div class="row">
                <div class="col-md-9 col-sm-8">
                    <div class="tab-content pt-0" id="v-pills-tabContent">
                        <div class="tab-pane fade active show" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab2">
                            <div class="row">
                                <div class="col-xl-5">
    
                                    <div class="tab-content pt-0">
                                        <div class="tab-pane active show" id="product-1-item">
                                            <img src="<?= base_url('assets/uploads/files/'. $row['file_gambar'] ) ?>" alt="" class="img-fluid mx-auto d-block rounded">
                                        </div>
                                    </div>
                                    
                                </div> <!-- end col -->
                                <div class="col-xl-7">
                                    <div class="pl-xl-3 mt-3 mt-xl-0">
                                        <a href="#" class="text-primary"><?= $row['nama_kategori'] ?></a>
                                        <h4 class="mb-3"><?= $row['nama_produk'] ?></h4>
                                        <!-- <p class="mb-4"><a href="" class="text-muted">( 36 Customer Reviews )</a></p> -->
                                        <!-- <h6 class="text-danger text-uppercase">20 % Off</h6> -->
                                        <h4 class="mb-4">Price : <span class="text-muted mr-2"><del>RP. <?= number_format($row['harga_coret'],0,',','.'); ?></del></span> <b><?= number_format($row['harga_produk'],0,',','.'); ?></b></h4>
                                        <h4><span class="badge bg-soft-success text-success mb-4"><?= $row['stok'] ?></span></h4>
                                        <p class="text-muted mb-4"><?= $row['deskripsi_produk'] ?></p>

                                        <div>
                                            <a href="<?= base_url('data/index/gambar/'. $id_produk)?>" class="btn btn-danger waves-effect waves-light"  target="_blank"><i class="mdi mdi-heart-outline"></i> Lihat Gambar</a>
                                            <a href="https://valuz.id/lp.php?id=<?= $row['id_produk']?>" class="btn btn-success waves-effect waves-light"  target="_blank">
                                                <span class="btn-label"><i class="mdi mdi-eye"></i></span>Lihat Landing Page
                                            </a>
                                        </div>
                                    </div>
                                </div> <!-- end col -->
                            </div>
                        <?php

                            }
                        }
                        ?>
                        <form action=""></form>
                        </div>
                        <div class="tab-pane fade" id="v-pills-headline" role="tabpanel" aria-labelledby="v-pills-profile-headline">
                            <div class="form-group mb-3">
                                <label for="product-reference">Headline <span class="text-danger">*</span></label>
                                <input type="text" id="headline" name="headline" class="form-control" placeholder="Input Headline" value="<?= $row['headline'] ?>">
                            </div>
                            <div class="form-group mb-3">
                                <label for="product-reference">Subheadline <span class="text-danger">*</span></label>
                                <textarea name="subheadline" id="subheadline" cols="30" rows="3"><?= $row['subheadline'] ?></textarea>
                                <form action="<?= base_url('product/upload_gambar/subheadline/' . $id_produk) ?>" method="post" class="dropzone dz-clickable" id="dzheadline"  name="dzheadline">
                                    <div class="dz-message needsclick">
                                        <i class="h1 text-muted dripicons-cloud-upload"></i>
                                        <h3>Drop files here or click to upload.</h3>
                                        <span class="text-muted font-13">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
                                    </div>
                                    
                                    <div class="text-right">
                                        <a href="<?= base_url('data/index/gambar/' . $id_produk . '/subheadline') ?>" class="btn btn-primary" target="_blank"><i class="fe-image"></i> Lihat Gambar</a>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div class="tab-pane fade" id="v-pills-masalah" role="tabpanel" aria-labelledby="v-pills-masalah-tab2">
                            
                            <div class="form-group mb-3">
                                <label for="masalah">Masalah <span class="text-danger">*</span></label>
                                <textarea name="masalah" id="masalah" cols="30" rows="3"><?= $row['masalah'] ?></textarea>
                                <form action="<?= base_url('product/upload_gambar/masalah/' . $id_produk) ?>" method="post" class="dropzone dz-clickable" id="dzmasalah">
                                    <div class="dz-message needsclick">
                                        <i class="h1 text-muted dripicons-cloud-upload"></i>
                                        <h3>Drop files here or click to upload.</h3>
                                        <span class="text-muted font-13">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
                                    </div>
                                    
                                    <div class="text-right">
                                        <a href="<?= base_url('data/index/gambar/' . $id_produk . '/masalah') ?>" class="btn btn-primary" target="_blank"><i class="fe-image"></i> Lihat Gambar</a>
                                    </div>
                                </form>
                            </div>

                        </div>
                        <div class="tab-pane fade" id="v-pills-solusi" role="tabpanel" aria-labelledby="v-pills-solusi-tab2">
                            
                            <div class="form-group mb-3">
                                <label for="solusi">Solusi <span class="text-danger">*</span></label>
                                <textarea name="solusi" id="solusi" cols="30" rows="3"><?= $row['solusi'] ?></textarea>
                                <form action="<?= base_url('product/upload_gambar/solusi/' . $id_produk) ?>" method="post" class="dropzone dz-clickable" id="dzsolusi">
                                    <div class="dz-message needsclick">
                                        <i class="h1 text-muted dripicons-cloud-upload"></i>
                                        <h3>Drop files here or click to upload.</h3>
                                        <span class="text-muted font-13">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
                                    </div>
                                    
                                    <div class="text-right">
                                        <a href="<?= base_url('data/index/gambar/' . $id_produk . '/solusi') ?>" class="btn btn-primary" target="_blank"><i class="fe-image"></i> Lihat Gambar</a>
                                    </div>
                                </form>
                            </div>
                            
                        </div>
                        <div class="tab-pane fade" id="v-pills-manfaat" role="tabpanel" aria-labelledby="v-pills-manfaat-tab2">
                            
                            <div class="form-group mb-3">
                                <label for="manfaat">Manfaat Produk <span class="text-danger">*</span></label>
                                <textarea name="manfaat" id="manfaat" cols="30" rows="3"><?= $row['manfaat'] ?></textarea>
                                <form action="<?= base_url('product/upload_gambar/manfaat/' . $id_produk) ?>" method="post" class="dropzone dz-clickable" id="manfaat-dropzone">
                                    <div class="dz-message needsclick">
                                        <i class="h1 text-muted dripicons-cloud-upload"></i>
                                        <h3>Drop files here or click to upload.</h3>
                                        <span class="text-muted font-13">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
                                    </div>
                                    
                                    <div class="text-right">
                                        <a href="<?= base_url('data/index/gambar/' . $id_produk . '/manfaat') ?>" class="btn btn-primary" target="_blank"><i class="fe-image"></i> Lihat Gambar</a>
                                    </div>
                                </form>
                            </div>
                            
                        </div>

                        <div class="tab-pane fade" id="v-pills-penawaran" role="tabpanel" aria-labelledby="v-pills-penawaran-tab2">
                            
                            <div class="form-group mb-3">
                                <label for="penawaran">Penawaran <span class="text-danger">*</span></label>
                                <textarea name="penawaran" id="penawaran" cols="30" rows="3"><?= $row['penawaran'] ?></textarea>
                                <form action="<?= base_url('product/upload_gambar/penawaran/' . $id_produk) ?>" method="post" class="dropzone dz-clickable" id="dzpenawaran">
                                    <div class="dz-message needsclick">
                                        <i class="h1 text-muted dripicons-cloud-upload"></i>
                                        <h3>Drop files here or click to upload.</h3>
                                        <span class="text-muted font-13">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
                                    </div>
                                    <div class="text-right">
                                        <a href="<?= base_url('data/index/gambar/' . $id_produk . '/penawaran') ?>" class="btn btn-primary" target="_blank"><i class="fe-image"></i> Lihat Gambar</a>
                                    </div>
                                </form>
                            </div>
                            
                        </div>
                        <div class="tab-pane fade" id="v-pills-spesifikasi" role="tabpanel" aria-labelledby="v-pills-spesifikasi-tab2">
                            
                            <div class="form-group mb-3">
                                <label for="spesifikasi">Spesifikasi Produk <span class="text-danger">*</span></label>
                                <textarea name="spesifikasi" id="spesifikasi" cols="30" rows="3"><?= $row['spesifikasi'] ?></textarea>
                                <form action="<?= base_url('product/upload_gambar/spesifikasi/' . $id_produk) ?>" method="post" class="dropzone dz-clickable" id="dzspesifikasi">
                                    <div class="dz-message needsclick">
                                        <i class="h1 text-muted dripicons-cloud-upload"></i>
                                        <h3>Drop files here or click to upload.</h3>
                                        <span class="text-muted font-13">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
                                    </div>
                                    <div class="text-right">
                                        <a href="<?= base_url('data/index/gambar/' . $id_produk . '/spesifikasi') ?>" class="btn btn-primary" target="_blank"><i class="fe-image"></i> Lihat Gambar</a>
                                    </div>
                                </form>
                            </div>
                            
                        </div>
                    </div>
                </div> <!-- end col -->
                <div class="col-md-3 col-sm-4">
                    <div class="nav flex-column nav-pills nav-pills-tab" id="v-pills-tab2" role="tablist" aria-orientation="vertical">
                        <a class="nav-link active show mb-2" id="v-pills-home-tab2" data-toggle="pill" href="#v-pills-home" role="tab" aria-controls="v-pills-home2" aria-selected="true">
                            Home</a>
                        <a class="nav-link mb-2" id="v-pills-headline-tab2" data-toggle="pill" href="#v-pills-headline" role="tab" aria-controls="v-pills-headline" aria-selected="false">
                            Headline</a>
                        <a class="nav-link mb-2" id="v-pills-masalah-tab2" data-toggle="pill" href="#v-pills-masalah" role="tab" aria-controls="v-pills-masalah" aria-selected="false">
                            Masalah</a>
                        <a class="nav-link mb-2" id="v-pills-solusi-tab2" data-toggle="pill" href="#v-pills-solusi" role="tab" aria-controls="v-pills-solusi" aria-selected="false">
                            Solusi</a>
                        <a class="nav-link mb-2" id="v-pills-manfaat-tab2" data-toggle="pill" href="#v-pills-manfaat" role="tab" aria-controls="v-pills-manfaat" aria-selected="false">
                            Manfaat Produk</a>
                        <a class="nav-link mb-2" id="v-pills-penawaran-tab2" data-toggle="pill" href="#v-pills-penawaran" role="tab" aria-controls="v-pills-penawaran" aria-selected="false">
                            Penawaran</a>
                        <a class="nav-link mb-2" id="v-pills-spesifikasi-tab2" data-toggle="pill" href="#v-pills-spesifikasi" role="tab" aria-controls="v-pills-spesifikasi" aria-selected="false">
                            Spesifikasi Produk</a>
                    </div>

                </div> <!-- end col -->

            </div> <!-- end row-->

        </div> <!-- end card-box-->
    </div>
</div>
</form>
<script>
</script>