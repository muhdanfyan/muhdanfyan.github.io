<!-- start page title -->
<div class="row">
        <div class="col-12">
            <div class="page-title-box">
                <div class="page-title-right">
                    <ol class="breadcrumb m-0">
                        <li class="breadcrumb-item"><a href="javascript: void(0);">UBold</a></li>
                        <li class="breadcrumb-item"><a href="javascript: void(0);">eCommerce</a></li>
                        <li class="breadcrumb-item active">Product Edit</li>
                    </ol>
                </div>
                <h4 class="page-title">Add / Edit Product</h4>
            </div>
        </div>
    </div>     
    <!-- end page title --> 


    <div class="row justify-content-center">
        <div class="col-lg-6">
            <div class="card-box">
                <h5 class="text-uppercase bg-light p-2 mt-0 mb-3">General</h5>
                <form action="<?= base_url('product/input') ?>" method="post">
                    <div class="form-group mb-3">
                        <label for="product-name">Nama Produk <span class="text-danger">*</span></label>
                        <input type="text" id="nama_produk" name="nama_produk" class="form-control" placeholder="Cth : Handphone, dlln.">
                    </div>

                    <div class="form-group mb-3">
                        <label class="mb-2">Status Barang <span class="text-danger">*</span></label>
                        <br/>
                        <div class="radio form-check-inline">
                            <input type="radio" id="inlineRadio1" value="option1" name="radioInline" checked="">
                            <label for="inlineRadio1"> Ready </label>
                        </div>
                        <div class="radio form-check-inline">
                            <input type="radio" id="inlineRadio2" value="option2" name="radioInline">
                            <label for="inlineRadio2"> Habis </label>
                        </div>
                    </div>

                    <div class="form-group mb-3">
                        <label for="product-reference">Berat <span class="text-danger">*</span></label>
                        <input type="text" id="berat" name="berat" class="form-control" placeholder="Berat Satuan Kilogram">
                    </div>

                    <div class="form-group mb-3">
                        <label for="harga_modal">Harga Modal <span class="text-danger">*</span></label>
                        <input type="number" class="form-control" id="harga_modal" name="harga_modal" placeholder="Harga Modal">
                    </div>
                    <div class="form-group mb-3">
                        <label for="harga_produk">Harga Produk <span class="text-danger">*</span></label>
                        <input type="number" class="form-control" id="harga_produk" name="harga_produk" placeholder="Harga Produk">
                    </div>

                    <div class="form-group mb-3">
                        <label for="harga_coret">Harga Coret <span class="text-danger">*</span></label>
                        <input type="number" class="form-control" id="harga_coret" name="harga_coret" placeholder="Harga Produk">
                    </div>

                    <div class="form-group mb-3">
                        <label for="product-category">Kategori <span class="text-danger">*</span></label>
                        <select class="form-control select2" id="kategori" nama="kategori">
                            <option style="color:#eee;">Pilih Kategori</option>
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
                        <label for="deskripsi">Deskripsi <span class="text-danger">*</span></label>
                        <textarea class="form-control" id="deskripsi"  name="deskripsi" rows="5" placeholder="Please enter description"></textarea>
                    </div>

                    <div class="text-center mb-3">
                        <button type="reset" class="btn w-sm btn-light waves-effect">Cancel</button>
                        <button type="button" class="btn w-sm btn-success waves-effect waves-light" id="simpan">Save</button>
                        <button type="button" class="btn w-sm btn-danger waves-effect waves-light">Delete</button>
                    </div>
                </form>
            </div> <!-- end card-box -->
        </div> <!-- end col -->

        <div class="col-lg-6" id="upload_gambar">
            
            <div class="card-box">
                <h5 class="text-uppercase mt-0 mb-3 bg-light p-2">Detail Produk</h5>

                <form action="/" method="post" class="dropzone" id="myAwesomeDropzone">
                    <div class="fallback">
                        <input name="file" type="file" multiple />
                    </div>

                    <div class="form-group mb-3">
                        <label for="headline">Headline</label>
                        <input type="text" class="form-control" id="headline"  name="headline" placeholder="Headline">
                    </div>
                    
                    <div class="form-group mb-3">
                        <label for="subheadline">Subheadline</label>
                        <textarea class="form-control" rows="3" id="subheadline" placeholder="Masukkan Sub Headline"></textarea>
                    </div>
                    
                    <div class="dz-message needsclick">
                        <i class="h1 text-muted dripicons-cloud-upload"></i>
                        <h3>Masukkan Gambar Untuk Headline</h3>
                        <span class="text-muted font-13">Drag Gambar ke sini dengan ukuran (..x..)</span>
                    </div>
                </form>

            </div> <!-- end col-->

            <div class="card-box">
                <h5 class="text-uppercase mt-0 mb-3 bg-light p-2">Meta Data</h5>

                <div class="form-group mb-3">
                    <label for="product-meta-title">Meta title</label>
                    <input type="text" class="form-control" id="product-meta-title" placeholder="Enter title">
                </div>

                <div class="form-group mb-3">
                    <label for="product-meta-keywords">Meta Keywords</label>
                    <input type="text" class="form-control" id="product-meta-keywords" placeholder="Enter keywords">
                </div>

                <div class="form-group mb-0">
                    <label for="product-meta-description">Meta Description </label>
                    <textarea class="form-control" rows="5" id="product-meta-description" placeholder="Please enter description"></textarea>
                </div>
            </div> <!-- end card-box -->

        </div>
        <!-- end col-->
    </div>
    <!-- end row -->

    <div class="row">
        <div class="col-12">

        </div> <!-- end col -->
    </div>
    <!-- end row -->

    

<script>
    $('#upload_gambar').hide();
    $('#simpan').on('click', function(){
        $('#upload_gambar').show();
    });
</script>