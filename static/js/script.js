// Script JavaScript para o Sabor Express

// Função para executar quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', function() {
    console.log('Sabor Express - Frontend carregado com sucesso!');
    
    // Auto-fechamento dos alertas após 5 segundos
    const alertList = document.querySelectorAll('.alert');
    alertList.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // Adiciona animação de hover nas linhas da tabela
    const tableRows = document.querySelectorAll('tbody tr');
    if (tableRows) {
        tableRows.forEach(row => {
            row.addEventListener('mouseenter', function() {
                this.style.backgroundColor = '#fff9e6';
                this.style.transition = 'background-color 0.3s ease';
            });
            
            row.addEventListener('mouseleave', function() {
                this.style.backgroundColor = '';
            });
        });
    }
    
    // Confirmação antes de alterar o estado de um restaurante
    const toggleButtons = document.querySelectorAll('a[href*="alterar_estado"]');
    if (toggleButtons) {
        toggleButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                const isActive = this.classList.contains('btn-danger');
                const action = isActive ? 'desativar' : 'ativar';
                const restaurantName = this.closest('tr').querySelector('td:first-child').textContent;
                
                if (!confirm(`Deseja realmente ${action} o restaurante "${restaurantName}"?`)) {
                    event.preventDefault();
                }
            });
        });
    }
    
    // Validação do formulário de cadastro
    const cadastroForm = document.querySelector('form[action*="cadastrar"]');
    if (cadastroForm) {
        cadastroForm.addEventListener('submit', function(event) {
            const nomeInput = document.getElementById('nome');
            const categoriaInput = document.getElementById('categoria');
            
            if (nomeInput.value.trim().length < 3) {
                event.preventDefault();
                alert('O nome do restaurante deve ter pelo menos 3 caracteres.');
                nomeInput.focus();
                return false;
            }
            
            if (!categoriaInput.value) {
                event.preventDefault();
                alert('Por favor, selecione uma categoria.');
                categoriaInput.focus();
                return false;
            }
            
            return true;
        });
    }
});