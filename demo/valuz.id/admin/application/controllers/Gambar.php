<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Gambar extends CI_Controller {

	function __construct()
	{
		parent::__construct();
        
        $this->load->library('Image_CRUD');    
		$this->load->helper('url');

		$this->_init();
	}

	private function _init()
	{
		$this->output->set_template('table');

		$this->load->js('assets/themes/default/js/jquery-1.9.1.min.js');
		$this->load->js('assets/themes/default/hero_files/bootstrap-transition.js');
		$this->load->js('assets/themes/default/hero_files/bootstrap-collapse.js');
    }
    
    public function index($tes=NULL){
        // instance object
        $image_crud = new image_CRUD();

        $image_crud->set_table('gambar');
        
        //If your table have by default the "id" field name as a primary key this line is not required
        $image_crud->set_primary_key_field('id_gambar');
        
        $image_crud->set_url_field('file_gambar');
        $image_crud->set_image_path('assets/uploads');
        $image_crud->set_ordering_field('urutan');
        $image_crud->set_ordering_field('produk', 'produk', 'file_gambar');
        $output = $image_crud->render();
        
        $this->load->view('data', $output);
    }
    public function produk ($tes=NULL){
        // instance object
        $image_crud = new image_CRUD();

        $image_crud->set_table('gambar');
        
        //If your table have by default the "id" field name as a primary key this line is not required
        $image_crud->set_primary_key_field('id_gambar');
        
        $image_crud->set_url_field('file_gambar');
        $image_crud->set_image_path('assets/uploads');
        $image_crud->set_ordering_field('urutan');
        // if (isset($tes))
            $image_crud->set_ordering_field('produk', 'produk', 'file_gambar');
        $output = $image_crud->render();
        
        $this->load->view('data', $output);
    }
}