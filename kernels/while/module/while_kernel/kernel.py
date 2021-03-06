from ipykernel.kernelbase import Kernel
import subprocess
import html

class WhileKernel(Kernel):
    implementation = 'While'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "This kernel will work while true"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        p = subprocess.run("WhileParser",
            stdout=subprocess.PIPE,
            input=code,
            encoding='ascii'
            )

        if not silent:
            if code == "restart":
                self.send_response(self.iopub_socket, 'display_data', {    
                    'data': {
                        'text/html': "<script>Jupyter.notebook.kernel.restart()</script>"
                    },
                    'metadata': {}
                })
            else:
                #stream_content = {'name': 'stdout', 'text': "<h1>html data</h1>"}
                display_data_content = {    
                    'data': {
                        'text/plain': p.stdout,
                        'text/html': "test: <p>" + html.escape(p.stdout) + "</p>"
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
