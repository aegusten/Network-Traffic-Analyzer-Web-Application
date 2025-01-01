/*!
 * FileInput Chinese Translations
 *
 * This file must be loaded after 'fileinput.js'. Patterns in braces '{}', or
 * any HTML markup tags in the messages must not be converted or translated.
 *
 * @see http://github.com/kartik-v/bootstrap-fileinput
 * @author kangqf <kangqingfei@gmail.com>
 *
 * NOTE: this file must be saved in UTF-8 encoding.
 */
(function ($) {
    "use strict";

    $.fn.fileinput.locales.en = {
        fileSingle: 'File',
        filePlural: 'Files',
        browseLabel: 'Browse &hellip;',
        removeLabel: 'Remove',
        removeTitle: 'Clear selected files',
        cancelLabel: 'Cancel',
        cancelTitle: 'Cancel ongoing upload',
        uploadLabel: 'Upload',
        uploadTitle: 'Upload selected files',
        msgSizeTooLarge: 'File "{name}" (<b>{size} KB</b>) exceeds the allowed size of <b>{maxSize} KB</b>. Please upload again!',
        msgFilesTooLess: 'You must select at least <b>{n}</b> {files} to upload. Please upload again!',
        msgFilesTooMany: 'The number of files selected for upload <b>({n})</b> exceeds the maximum limit of <b>{m}</b>. Please upload again!',
        msgFileNotFound: 'File "{name}" not found!',
        msgFileSecured: 'Security restrictions prevent reading the file "{name}".',
        msgFileNotReadable: 'File "{name}" is not readable.',
        msgFilePreviewAborted: 'Preview canceled for "{name}".',
        msgFilePreviewError: 'An error occurred while reading "{name}".',
        msgInvalidFileType: 'Invalid type for "{name}". Only "{types}" files are supported.',
        msgInvalidFileExtension: 'Invalid file extension for "{name}". Only files with extensions "{extensions}" are supported.',
        msgValidationError: 'File upload error',
        msgLoading: 'Loading file {index} of {files} &hellip;',
        msgProgress: 'Loading file {index} of {files} - {name} - {percent}% completed.',
        msgSelected: '{n} {files} selected',
        msgFoldersNotAllowed: 'Drag & drop only files! Skipped {n} dragged folders.',
        dropZoneTitle: 'Drag & drop files here &hellip;',
        slugCallback: function(text) {
            return text ? text.split(/(\\|\/)/g).pop().replace(/[^\w\-.\\/ ]+/g, '') : '';
        }
    };    

    $.extend($.fn.fileinput.defaults, $.fn.fileinput.locales.zh);
})(window.jQuery);
