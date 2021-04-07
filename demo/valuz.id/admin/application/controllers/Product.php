<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Product extends CI_Controller {

	function __construct()
	{
		parent::__construct();
		
		$this->lang->load('auth');
		$this->_init();
	}

	private function _init(){
		$this->output->set_template('ubold');

		$this->load->js('assets/themes/default/js/jquery-1.9.1.min.js');
		$this->load->js('assets/themes/default/hero_files/bootstrap-transition.js');
		$this->load->js('assets/themes/default/hero_files/bootstrap-collapse.js');
    }
    
    public function index(){
		if (!$this->ion_auth->logged_in())
		{
			// redirect them to the login page
			redirect('auth/login', 'refresh');
		}
		else if (!$this->ion_auth->is_admin()) // remove this elseif if you want to enable this for non-admins
		{
			// redirect them to the home page because they must be an administrator to view this
			show_error('You must be an administrator to view this page.');
		}
		else
		{

			$data['dataproduk'] = $this->db->get('produk');
			$data['kategori'] = $this->db->get('kategori');
			$this->load->view('product/list', $data);
		}
    }

    public function input($id_produk=NULL){
		if (isset($id_produk)){
			$data['tampil'] = TRUE;
		}
		$data['kategori'] = $this->db->get('kategori');
        $this->load->view('product/add', $data);  
	}
	
    public function insert(){
		$insert['nama_produk'] = $this->input->post('nama_produk');
		$insert['stok'] = $this->input->post('stok');
		$insert['berat'] = $this->input->post('berat');
		$insert['harga_modal'] = $this->input->post('harga_modal');
		$insert['harga_produk'] = $this->input->post('harga_produk');
		$insert['harga_coret'] = $this->input->post('harga_coret');
		$insert['kategori_produk'] = $this->input->post('kategori');
		$insert['deskripsi_produk'] = $this->input->post('deskripsi');
		// $insert['nama_produk'] = $this->input->post('nama_produk');
		// $insert['nama_produk'] = $this->input->post('nama_produk');

		$config['upload_path'] = './assets/uploads/files/';
		$config['allowed_types']= 'gif|jpg|png|jpeg';
		$config['encrypt_name']	= TRUE;
		$config['remove_spaces']= TRUE;	
		$config['max_size']     = '3000';
		$config['max_width']  	= '1000';
		$config['max_height']  	= '1000';

		$this->load->library('upload', $config);
		if($this->upload->do_upload("file_gambar"))
		{
			$data	 	= $this->upload->data();
			echo "<script>alert ('sudah upload');</script>";
		}
		else
			redirect('produk','refresh');
		
		
		$insert['file_gambar'] = $data['file_name'];;
		
		$this->db->insert('produk', $insert);

		redirect("product/detail_edit/" . $this->db->insert_id());
	}


    public function delete($id){
		$this->db->query("DELETE from produk where id_produk=$id");
		redirect('product');		
	}

	public function detail_edit($id_produk=NULL){
		if (isset($id_produk)){
			$this->db->join('kategori', 'produk.kategori_produk = kategori.id_kategori', 'left');
			$this->db->where('id_produk', $id_produk);
			$data['dataproduk'] = $this->db->get('produk', 1, 0);
			$data['id_produk'] = $id_produk;
		}
		
        $this->load->view('product/detail-edit', $data);  
	}

	public function update($id_produk){
		$data['headline'] 		= $this->input->post('headline');
		$data['subheadline']	= $this->input->post('subheadline');
		$data['masalah'] 		= $this->input->post('masalah');
		$data['solusi'] 		= $this->input->post('solusi');
		$data['manfaat'] 		= $this->input->post('manfaat');
		$data['penawaran'] 		= $this->input->post('penawaran');
		$data['spesifikasi'] 	= $this->input->post('spesifikasi');

		$this->db->where('id_produk', $id_produk);
		$this->db->update('produk', $data);

		redirect('product/detail_edit/'. $id_produk);
		// $this->output->enable_profiler(TRUE);
	}

	public function upload_gambar($kriteria, $id_produk){
	
		if(!empty($_FILES['file']['name'])){

			// Set preference
			$config['upload_path'] = 'assets/uploads/files/';
			$config['allowed_types'] = 'jpg|jpeg|png|gif';
			$config['max_size'] = '3000'; // max_size in kb
			$config['file_name'] = sprintf("%05d", $id_produk) . $kriteria . "_" . $_FILES['file']['name'];
	   
			//Load upload library
			$this->load->library('upload',$config); 
	   
			// File upload
			if($this->upload->do_upload('file')){
			  // Get data about the file
			  $uploadData = $this->upload->data();
			  $data['file_gambar'] = $config['file_name'];
			  $data['produk'] = $id_produk;
			  $data['kriteria'] = $kriteria;

			  $this->db->insert('gambar', $data);
			}
		  }
	}

}