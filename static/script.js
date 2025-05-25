function readTextFile(input, callback) {
    const file = input.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (e) {
        callback(e.target.result);
    };
    reader.readAsText(file);
}

$(document).ready(function () {
    $('#equationFiles').on('change', function () {
    const files = this.files;
    if (!files.length) return;

    let fileContents = [];

    let loaded = 0;
    for (let i = 0; i < files.length; i++) {
        const reader = new FileReader();
        reader.onload = function (e) {
            fileContents[i] = e.target.result.trim();
            loaded++;
            if (loaded === files.length) {
                const combined = fileContents.join('\n---\n');
                $('#equations').val(combined);
            }
        };
        reader.readAsText(files[i]);
    }
    });

    $('#constantsFile').change(function () {
        readTextFile(this, function (text) {
            $('#constants').val(text);
        });
    });

    $('#solveBtn').click(function () {
        const solver = $('#solver').val();
        const equations = $('#equations').val();
        const constants = $('#constants').val();

        $.ajax({
            url: '/solve',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                solver: solver,
                equations: equations,
                constants: constants
            }),
            success: function (response) {
                if (response.success) {
                    $('#solutionBox').text(response.solution);
                } else {
                    $('#solutionBox').text("Error: " + response.error);
                }
            },
            error: function () {
                $('#solutionBox').text("An unexpected error occurred.");
            }
        });
    });
});
