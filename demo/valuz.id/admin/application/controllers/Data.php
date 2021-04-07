<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Data extends CI_Controller {

	function __construct()
	{
		parent::__construct();

		$this->load->helper('url');

		$this->_init();
	}

	private function _init()
	{
		$this->output->set_template('ubtable');
		// $this->output->set_template('default');

		$this->load->js('assets/themes/default/js/jquery-1.9.1.min.js');
		$this->load->js('assets/themes/default/hero_files/bootstrap-transition.js');
		$this->load->js('assets/themes/default/hero_files/bootstrap-collapse.js');
    }
    
    public function index($table=NULL, $indx=NULL, $kriteria=NULL){
        if (isset($table)){
            // instance object
            $crud = new grocery_CRUD();
            // pilih tabel yang akan digunakan
            $crud->set_table($table);
            // custom field yang ingin ditampilkan
            // $crud->columns('lastName','firstName','email');
            if ($table=="produk"){
                $crud->set_field_upload('file_gambar','assets/uploads/files');
                $crud->set_relation('kategori_produk','kategori','nama_kategori');
                $crud->display_as('harga_produk', 'Harga Jual');
                $crud->columns('nama_produk','file_gambar','harga_produk');
                $crud->add_action('Gambar', '', 'data/index/gambar', 'fa-file-image-o');
            }
            else if ($table=="gambar"){
                $crud->set_field_upload('file_gambar','assets/uploads/files/');
                $crud->set_relation('produk','produk','nama_produk');
                $crud->order_by('urutan','asc');
                if (isset($indx))
                    $crud->where('produk', $indx);
                if(isset($kriteria))
                    $crud->where('kriteria',$kriteria);
            }
            else if ($table=="slide"){
                $crud->set_field_upload('file_slide','assets/uploads/files');
                $crud->set_relation('produk','produk','nama_produk');
            }
            $crud->unset_fields('created_at','updated_at');
            $crud->unset_columns('created_at','updated_at');
            $crud->unset_read();
            // $crud->unset_clone();
            // simpan hasilnya kedalam variabel output
            $output = $crud->render();
            // tampilkan di view 
            $this->load->view('data', $output);
        }
        else
            $this->load->view('welcome_message');
    }
}