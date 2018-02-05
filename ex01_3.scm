#!/usr/local/bin/gosh
(define (read-file file-name)
  (call-with-input-file file-name port->string-list))

(define (main args)
  (use srfi-13)
  (let* ((file-name "NT_113952.1.fasta")
         (lst (read-file file-name))
         (sequence (apply string-append (cdr lst))))
    (print (format "A: ~a" (string-count sequence #\A)))
    (print (format "T: ~a" (string-count sequence #\T)))
    (print (format "G: ~a" (string-count sequence #\G)))
    (print (format "C: ~a" (string-count sequence #\C)))
    )
  0
  )
