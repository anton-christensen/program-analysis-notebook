from ipykernel.kernelbase import Kernel
import os
from graphviz import Digraph

class EchoKernel(Kernel):
    implementation = 'Echo'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "The echo kernel, by Anton"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if code == "restart":
                self.send_response(self.iopub_socket, 'display_data', {
                    'data': {
                        'text/html': "<script>Jupyter.notebook.kernel.restart()</script>"
                    },
                    'metadata': {}
                })

            elif code == "graph":
                graph = Digraph(format='svg')
                graph.format = 'svg';
                graph.node('1');
                graph.node('2');
                graph.edges(['12']);

                self.send_response(self.iopub_socket, 'display_data', {
                    'data': {
                        'image/svg+xml': graph.pipe().decode('utf-8')
                    },
                    'metadata': {}
                })
            else:

                #stream_content = {'name': 'stdout', 'text': "<h1>html data</h1>"}
                display_data_content = {
                    'data': {
                        'text/plain': code,
                        'text/html': "<b>"+code+"</b>"
                    },
                    'metadata': {}
                }
                #self.send_response(self.iopub_socket, 'stream', stream_content)
                self.send_response(self.iopub_socket, 'display_data', display_data_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
