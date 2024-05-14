$(document).ready(function() {
    $('#selecao').change(function() {
        
        $('#conteudo-salgados, #conteudo-doces').hide();

        
        var opcaoSelecionada = $(this).val();
        if (opcaoSelecionada) {
            $('#conteudo-' + opcaoSelecionada).show();
        }
    });
});
