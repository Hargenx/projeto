<?php

namespace App\Http\Controllers;

use App\Models\Pessoa;
use Illuminate\Http\Request;

class pessoaController extends Controller
{
    protected $pessoas;
    public function __construct(Pessoa $pessoas)
    {
        $this->pessoas = $pessoas;
    }

    //index está busacando todos os dados da pessoa
    public function index()
    {
        //logo faremos um $pessoas = $this->pessoas->paginate(3);
        $pessoas = $this->pessoas->all();
        //nomeado return view('pessoas.index', compact('pessoas'));
        return view('pessoas', ['pessoas' => $pessoas]);
    }
    //Metodo show está buscando um dado especifico
    public function show($id)
    {
        $pessoa = $this->pessoas->find($id);
        return view('buscapessoa', compact('pessoa'));
    }
    public function create()
    {
        return view('cadastrar');
    }
    public function posts(Request $request)
    {
        //podemos criar validações com o Request
        $request->validate([
            'nome' => 'required|min:3',
            'email' => 'required|email',
            'telefone' => 'required|min:8',
            'endereco' => 'required|min:3',
            'data_nascimento' => 'required|date'
        ]);
        $pessoa = $request->all();
        $this->pessoas->create($pessoa);
        return redirect()->route('listar')->with('success', 'Pessoa cadastrada com sucesso!');
    }
}
