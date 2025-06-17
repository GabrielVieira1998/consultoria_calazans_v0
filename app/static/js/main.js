// UTM Parameter Preservation
function preserveUTMParameters() {
    // Função para capturar parâmetros UTM da URL atual
    function getUTMParams() {
        const urlParams = new URLSearchParams(window.location.search);
        const utmParams = {};
        
        // Lista de parâmetros UTM válidos
        const utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
        
        utmKeys.forEach(key => {
            if (urlParams.has(key)) {
                utmParams[key] = urlParams.get(key);
            }
        });
        
        return utmParams;
    }
    
    // Função para salvar parâmetros UTM no sessionStorage
    function saveUTMParams(params) {
        if (Object.keys(params).length > 0) {
            sessionStorage.setItem('utm_params', JSON.stringify(params));
            console.log('UTM parameters saved:', params);
        }
    }
    
    // Função para recuperar parâmetros UTM do sessionStorage
    function getSavedUTMParams() {
        const saved = sessionStorage.getItem('utm_params');
        return saved ? JSON.parse(saved) : {};
    }
    
    // Função para detectar fonte baseada no referrer e UTM
    function detectSource(utmSource) {
        if (utmSource) return utmSource;
        
        const referrer = document.referrer.toLowerCase();
        if (referrer.includes('instagram.com')) return 'instagram';
        if (referrer.includes('facebook.com')) return 'facebook';
        if (referrer.includes('google.com')) return 'google';
        if (referrer.includes('whatsapp')) return 'whatsapp';
        if (referrer.includes('t.co')) return 'twitter';
        if (referrer.includes('linkedin.com')) return 'linkedin';
        
        return 'direct';
    }
    
    // Função para adicionar parâmetros UTM a um link
    function addUTMToLink(link, utmParams) {
        if (Object.keys(utmParams).length === 0) return;
        
        const url = new URL(link.href);
        Object.keys(utmParams).forEach(key => {
            url.searchParams.set(key, utmParams[key]);
        });
        link.href = url.toString();
    }
    
    // Capturar parâmetros UTM atuais
    const currentUTMParams = getUTMParams();
    
    // Se há parâmetros UTM na URL atual, salvá-los
    if (Object.keys(currentUTMParams).length > 0) {
        saveUTMParams(currentUTMParams);
    }
    
    // Recuperar parâmetros UTM salvos
    const savedUTMParams = getSavedUTMParams();
    
    // Adicionar parâmetros UTM a todos os links internos
    if (Object.keys(savedUTMParams).length > 0) {
        // Links da navegação principal
        const navLinks = document.querySelectorAll('.navbar-nav a.nav-link');
        navLinks.forEach(link => {
            // Só adicionar UTM para links internos (mesma origem)
            try {
                const linkUrl = new URL(link.href);
                if (linkUrl.origin === window.location.origin) {
                    addUTMToLink(link, savedUTMParams);
                }
            } catch (e) {
                // Link relativo ou inválido, assumir como interno
                if (!link.href.startsWith('http')) {
                    addUTMToLink(link, savedUTMParams);
                }
            }
        });
        
        // Links do footer
        const footerLinks = document.querySelectorAll('footer a');
        footerLinks.forEach(link => {
            try {
                const linkUrl = new URL(link.href);
                if (linkUrl.origin === window.location.origin) {
                    addUTMToLink(link, savedUTMParams);
                }
            } catch (e) {
                if (!link.href.startsWith('http')) {
                    addUTMToLink(link, savedUTMParams);
                }
            }
        });
        
        // Preencher campos hidden do formulário de contato se existir
        const contactForm = document.querySelector('#contactForm');
        if (contactForm) {
            // Preencher campos UTM existentes
            Object.keys(savedUTMParams).forEach(key => {
                const field = contactForm.querySelector(`input[name="${key}"]`);
                if (field) {
                    field.value = savedUTMParams[key];
                }
            });
            
            // Preencher campo source
            const sourceField = contactForm.querySelector('input[name="source"]');
            if (sourceField) {
                sourceField.value = detectSource(savedUTMParams.utm_source);
            }
            
            console.log('UTM parameters filled in contact form:', savedUTMParams);
        }
    }
}

// Fechar alertas automaticamente
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar preservação de UTM
    preserveUTMParameters();
    
    // Auto-close alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Validação personalizada para formulários
    const forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Máscara para campos de telefone
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(function(input) {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length > 0) {
                // Apply mask (XX) XXXXX-XXXX
                if (value.length <= 2) {
                    value = `(${value}`;
                } else if (value.length <= 7) {
                    value = `(${value.substring(0, 2)}) ${value.substring(2)}`;
                } else if (value.length <= 11) {
                    value = `(${value.substring(0, 2)}) ${value.substring(2, 7)}-${value.substring(7)}`;
                } else {
                    value = `(${value.substring(0, 2)}) ${value.substring(2, 7)}-${value.substring(7, 11)}`;
                }
                e.target.value = value;
            }
        });
    });

    // Animações ao scroll
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    function checkIfInView() {
        const windowHeight = window.innerHeight;
        const windowTopPosition = window.scrollY;
        const windowBottomPosition = windowTopPosition + windowHeight;
        
        animatedElements.forEach(function(element) {
            const elementHeight = element.offsetHeight;
            const elementTopPosition = element.offsetTop;
            const elementBottomPosition = elementTopPosition + elementHeight;
            
            // Check if element is in view
            if (
                (elementBottomPosition >= windowTopPosition) &&
                (elementTopPosition <= windowBottomPosition)
            ) {
                element.classList.add('animate-fade-in');
            }
        });
    }
    
    // Check on initial load
    checkIfInView();
    
    // Check on scroll
    window.addEventListener('scroll', checkIfInView);
}); 