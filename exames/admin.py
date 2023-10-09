from django.contrib import admin
from .models import TiposExame, SolicitacaoExame, PedidosExames, AcessoMedico


admin.site.register(TiposExame)
admin.site.register(SolicitacaoExame)
admin.site.register(PedidosExames)
admin.site.register(AcessoMedico)
